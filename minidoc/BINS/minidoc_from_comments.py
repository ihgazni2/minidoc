from minidoc import minidoc
from minidoc import tst
from minidoc import comast
import argparse
from efdir import fs

parser = argparse.ArgumentParser()
parser.add_argument('-src','--src_file', default="code.src.py",help=".src.py file name")
parser.add_argument('-codec','--codec', default="utf-8",help=".tst.py file codec")
parser.add_argument('-dst','--dst_dir', default="./code.src.rst",help="destination rst")
parser.add_argument('-proj','--proj_name', default="projname",help="project name")
parser.add_argument('-desc','--proj_desc', default="desc0\ndesc1",help="project description")
parser.add_argument('-lic','--proj_lic', default="MIT",help="project license")
parser.add_argument('-inst','--proj_inst_cmd', default="",help="project install cmd")
parser.add_argument('-tbot','--title_bot', default="=",help="parent title bottom char")
parser.add_argument('-ebot','--entry_bot', default="-",help="entry title bottom char")


def boolize(s):
    s = s.lower()
    if(s=="true"):
        return(True)
    elif(s=="false"):
        return(False)
    else:
        return(False)

args = parser.parse_args()


def main():
    projhd = tst.creat_projhd(args.proj_name,args.proj_desc)
    install = tst.creat_install(args.proj_name)
    license = tst.creat_license(args.proj_lic)
    #kl = func_names
    #vl = comments  
    usage = tst.creat_rst(kl,vl)
    rst_str = projhd + install + license + usage
    fs.wfile(args.proj_name+".rst",rst_str,codec=args.codec)
