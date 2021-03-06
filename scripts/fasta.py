#!/usr/bin/python

class Fasta:
    
    def __init__(self,fasta_file):
        self.file = fasta_file
        self.sequences = {}
    
    def load(self):
        fasta = open(self.file, "r").readlines()
        for line in fasta:
            if line[0] == ">":
                name = line[1:].rstrip()
                self.sequences[name] = ""
            else:
                self.sequences[name] += line.rstrip().upper()
        #for name,seq in self.sequences.items():
            #self.sequences[name] = seq.capitalize()
            
        return self.sequences
    
    def get_names(self):
        return self.load().keys()
    
    def get_sequences(self):
        return self.load().values()

