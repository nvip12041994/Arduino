#define PORT Serial //USB
//#define DBG_PORT Serial
#define UART_RX_BUFFER_LEN 15

boolean stringComplete = false;
char rx_buff[UART_RX_BUFFER_LEN];
unsigned int rx_count = 0;
unsigned int msg_line = 0;
char msg_recv[8][UART_RX_BUFFER_LEN];

void(* reset) (void) = 0;

void setup()
{
  hw_init();
  PORT.begin(115200);
  #if defined(DEBUG)
    DBG_PORT.begin(115200);
  #endif
}

void loop()
{
  char* message;
  unsigned int gpio;
  char direct;
  char value;
  unsigned int i,j, cnt;
//  PORT.println("This is Arduino test message");
//  if(PORT.available()) serialEvent_();
  if(stringComplete)
  {
    stringComplete = false;
    for(i = 0; i < 8; i++)
    {
      if(msg_recv[i][0] != '\0')
      {
        #if defined(DEBUG)
          DBG_PORT.println(message);
        #endif
        switch(msg_recv[i][1])
        {
          case 'S':
            if(msg_recv[i][4] == '_')
            {
              gpio = msg_recv[i][3] - 48;
              direct = msg_recv[i][5];
              value = msg_recv[i][7];
            }
            else
            {
              gpio = (msg_recv[i][3] - 48) * 10 + (msg_recv[i][4] - 48);
              direct = msg_recv[i][6];
              value = msg_recv[i][8];
            }
            set_gpio(gpio, direct, value);
            msg_recv[i][0] = '\0';
            break;
          case 'R':
            hw_init();
            break;
        }
      }
    }
  }
}

void serialEvent()
{
  unsigned int i;
  char inChar;
  //if(PORT.available())
  {
    inChar = (char)PORT.read();
    //PORT.write(inChar);
    if((rx_count == 0 && inChar == '?') || (msg_recv[msg_line][0] == '?' && rx_count < UART_RX_BUFFER_LEN))
    {
      if(inChar == '?')
      {
        rx_count = 0;
      }
      msg_recv[msg_line][rx_count] = inChar;
      rx_count++;
    }
    else
    {
      msg_recv[msg_line][0] = '\0';
      rx_count = 0;
    }
    if(rx_count != 0 && msg_recv[msg_line][rx_count-1] == '^')
    {
      stringComplete = true;
      msg_recv[msg_line][rx_count-1] = '\0';
      rx_count = 0;
      for(i = 0;i < 8; i++)
      {
        if(msg_recv[i][0] == '\0')
        {
          msg_line = i;
          break;
        }
      }
    }
    #if defined(DEBUG)
      DBG_PORT.print("   msg_line=");DBG_PORT.println((char)(msg_line + 48));
      DBG_PORT.print("    rx_count=");DBG_PORT.println((char)(rx_count + 48));
      if(stringComplete)
        DBG_PORT.println("    stringComplete=true");
      else
        DBG_PORT.println("    stringComplete=false");
      DBG_PORT.println(" ");
    #endif
  }
}

void set_gpio(unsigned int gpio, char direct, char value)
{
  if(direct == 'I')
  {
    pinMode(gpio, INPUT);
  }
  else
  {
    digitalWrite(gpio, value=='1'?HIGH:LOW);
    pinMode(gpio, OUTPUT);
  }
}

void hw_init()
{
  unsigned int i;
  for(i=2;i<54;i++)
  {
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
    pinMode(i, INPUT);
  }
  for(i=0;i<8;i++)
  {
    msg_recv[i][0] = '\0';
  }
}


