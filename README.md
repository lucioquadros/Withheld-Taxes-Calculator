## Synopsis

**Withheld Taxes Calculator** <br />
This program calculates the discounted amount from the invoice based on the withheld taxes (IR, PIS, COFINS and CSLL).

**Created by** Lúcio Quadros de Souza - 09/12/2016

## Motivation

NFe.io test requested by Gabriel Marquez

## Installation

**Requirements** <br />
Python 3

**Running** <br />
Execute *taxes.py* in the terminal. e.g.: python taxes.py

## HOW TO USE
If all the tax rates are applicable is necessary to define each one and input the initial invoice.<br />
To set the invoice simply type:<br />
<br />
invoice value<br />
e.g.: invoice 6000 -> the invoice is set to R$6000<br />
<br />
To set the various tax rates simply use 'name' 'value in percentage'<br />
e.g.: pis 30 -> The pis tax rate is set to 30%<br />
<br />
The commands are listed below:<br />
ir 'percentage value' -> to set the IR tax rate;<br />
pis 'percentage value' -> to set the PIS tax rate;<br />
cofins 'percentage value' -> to set the COFINS tax rate;<br />
csll 'percentage value' -> to set the CSLL tax rate;<br />
<br />
To calculate the final discounted amount simply type: calculate<br />
If help is needed, type: help, to show this text again.<br />
To exit type: close
