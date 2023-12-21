# Bitcoin-Script

## generate a requirements.txt file
```sh
$ pip install pipreqs
```
```sh
$ pipreqs .
```
## install required packages
```sh
$ pip install -r requirements.txt
```
## task1_spend.py
If there is any connection error when running the program
Try to run it again to broadcast tx

## task2_spend.py
If there is a error "relay fee not met" reported, please increase the fee in preparetx() function to the required amount.
E.g. relay fee not met, 200 < 398 --> change fee to 398 or higher