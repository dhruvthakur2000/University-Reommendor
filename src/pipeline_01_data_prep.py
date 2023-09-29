import os
import argparse
import yaml
import logging


if __name__=="__main__": #main entrance of file
    args=argparse.ArgumentParser()#adding arguments
    args.add_argument("--config",default="default") #adding config file as arguments
    args.add_argument("--datasource",default=None)#adding datasource  file as arguments
    
    parsed_args=args.parse_args()
    print(parsed_args)
    #When we call the parse_args method, it will return a Namespace object with two attributes, integers and accumulate . 