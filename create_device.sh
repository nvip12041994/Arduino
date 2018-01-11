#!/bin/bash

NUM=2
INPUT_DEVICE='/dev/ttyUSB1'
DEVICE=`echo $INPUT_DEVICE | sed 's/\/dev\/tty//'`
declare -A device_map
function create_socat_pair {
	socat -d -d pty,raw,echo=0 pty,raw,echo=0 > temp.tmp 2>&1 &
	sleep 1
	device=$(grep -o "/dev/pts/[0-9]*" temp.tmp)
	device=(${device[@]})
	
	rm temp.tmp

	device_map["${device[0]}"]=${device[1]}
}

function create_shortcut {
	echo "-- Create virtual shortcut tty"
	counter=1
	for key in ${!device_map[@]}; do
		target=$(echo ${key} | sed -e 's/^"//' -e 's/"$//')
		sudo ln -s ${target} /dev/tty$DEVICE$counter
		echo "Target ${target} "
		echo "##### /dev/tty$DEVICE$counter"
		echo "Key = ${key} device_map[${key}] = ${device_map[${key}]}"
		link=(${link[@]} ${device_map[${key}]})
		((counter++))
	done
}

function remove_shortcut {
	for ((i=1;i<=NUM;i++)); do
		sudo rm /dev/tty$DEVICE$i
	done
}


for ((i=1;i<=NUM;i++)); do
	create_socat_pair;
done

create_shortcut;

echo "-- Created $NUM socket pair(s)"

echo "========================"
echo ${link[0]}
echo ${link[1]}
old_tty_settings="$(stty -g)"
#(stty raw; cat > received.log) < $INPUT_DEVICE &



trap ctrl_c INT
echo "Waiting for Ctrl+C"

function ctrl_c() {
	echo ""
	echo "** Trapped CTRL-C"
	remove_shortcut
	stty "$old_tty_settings"
	exit
}



while true;do
	echo 1 > /dev/null
done
