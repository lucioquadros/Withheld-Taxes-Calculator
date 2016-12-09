'''
Program name:
    Withheld Taxes Calculator

Created by:
    Lucio Quadros de Souza - 09/12/2016

Description:
    This program calculates the discounted amount from the invoice based on the withheld taxes (IR, PIS, COFINS and CSLL).

Notes:
    NFe.io test requested by Gabriel Marquez

'''

import cmd

class taxesCommand(cmd.Cmd):
    '''Command processor interface'''

    prompt = '>>>'

    def do_invoice(self, line):
        global invoice

        try:
            if float(line) >= 0:
                invoice = float(line)
            else:
                print("The variable needs to be a number greater or equal to zero.")
        except:
            print("The variable needs to be a number.")

    def do_ir(self, line):
        global IR

        try:
            if float(line) >= 0:
                IR = float(line)
            else:
                print("The variable needs to be a number greater or equal to zero.")
        except:
            print("The variable needs to be a number.")

    def do_pis(self, line):
        global PIS

        try:
            if float(line) >= 0:
                PIS = float(line)
            else:
                print("The variable needs to be a number greater or equal to zero.")
        except:
            print("The variable needs to be a number.")

    def do_cofins(self, line):
        global COFINS

        try:
            if float(line) >= 0:
                COFINS = float(line)
            else:
                print("The variable needs to be a number greater or equal to zero.")
        except:
            print("The variable needs to be a number.")


    def do_csll(self, line):
        global CSLL

        try:
            if float(line) >= 0:
                CSLL = float(line)
            else:
                print("The variable needs to be a number greater or equal to zero.")
        except:
            print("The variable needs to be a number.")


    def do_calculate(self, line):

        try:
            if invoice*(IR/100) > 10:
                IR_amount = invoice*(IR/100)
            else:
                IR_amount = 0
            if invoice > 5000:
                PIS_amount = invoice*(PIS/100)
                COFINS_amount = invoice*(COFINS/100)
                CSLL_amount = invoice*(CSLL/100)
            else:
                PIS_amount = 0
                COFINS_amount = 0
                CSLL_amount = 0
            total = IR_amount + PIS_amount + COFINS_amount + CSLL_amount

            print ("\nIR Amount: %.2f" % round(IR_amount,2))
            print ("PIS Amount: %.2f" % round(PIS_amount,2))
            print ("COFINS Amount: %.2f" % round(COFINS_amount,2))
            print ("CSLL Amount: %.2f" % round(CSLL_amount,2))
            print ("\nTOTAL discounted: %.2f" % round(total,2))

        except:
            print("Please, define all the tax rates before proceeding.")

    def do_help(self, line):
        print("\n\t\t\t ======== Withheld Taxes Calculator ======== \n\n")
        print("This program calculates the discounted amount from the invoice based on the withheld taxes (IR, PIS, COFINS and CSLL).")
        print("The IR discount will be only withheld if the amount is greater than R$10, otherwise will be automaticaly set to ZERO. Likewise, PIS, COFINS and CSLL will only\
     be discounted if the initial invoice amount is greater than R$5000.")
        print("\n\t *HOW TO USE* \n")
        print("If all the tax rates are applicable is necessary to define each one and input the initial invoice. \nTo set the invoice simply type:")
        print("\ninvoice value \ne.g.: invoice 6000 -> the invoice is set to R$6000\n")
        print("To set the various tax rates simply use 'name' 'value in percentage' \n\ne.g.: pis 30 -> The pis tax rate is set to 30%\n\nThe commands are listed below:")
        print("ir 'percentage value' -> to set the IR tax rate;")
        print("pis 'percentage value' -> to set the PIS tax rate;")
        print("cofins 'percentage value' -> to set the COFINS tax rate;")
        print("csll 'percentage value' -> to set the CSLL tax rate;")
        print("\nTo calculate the final discounted amount simply type: calculate")
        print("If help is needed, type: help, to show this text again.")
        print("To exit type: close")

    def do_close(self, line):
        return True

if __name__ == '__main__':

    '''Main calculator help'''
    taxesCommand().do_help('help')

    '''Run command loop'''
    taxesCommand().cmdloop()
