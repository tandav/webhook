mkfifo pipe.fifo
while true; do eval "$(< pipe.fifo)"; done
