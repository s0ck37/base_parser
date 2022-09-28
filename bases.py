#!/usr/bin/env python3

from math import log

class Bases:

    def __init__(self):
        self.symbol_table = "0123456789abcdefghijklmnopqrstuvwxyz"

    def check_base(self,base):
        if(base > len(self.symbol_table)):
            raise Exception(f"Maximun supported base is {len(self.symbol_table)}") 

    def parse_number(self,target,base):
        self.check_base(base)
        total = 0
        target = (target[::-1]).lower()
        target_lenght = len(target)
        local_table = self.symbol_table[:base]
        for position in range(0,target_lenght):
            if(target[position] not in local_table):
                raise Exception(f"Digit '{target[position]}' not matching base {base}.")
            total += local_table.index(target[position])*(base**position)
        return total

    def new_base(self,target,base):
        self.check_base(base)
        final_number = ""
        new_lenght = int(log(target,base)) # Hago uso del logaritmo para saber la cantidad de digitos que tiene
        for i in range(new_lenght,-1,-1):
            final_number += self.symbol_table[ target//(base**(i)) ]
            target = target%( base**(i) )
        return final_number
