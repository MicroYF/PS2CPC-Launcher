from cgi import test
from ctypes.wintypes import POINT
from lib2to3.pgen2.pgen import generate_grammar
from multiprocessing import set_forkserver_preload
import os
from re import L
import re
from sys import setrecursionlimit
from tarfile import LENGTH_LINK

from pyparsing import line



class Length():
    
    def __init__(self):
        self.readline_hash()
        self.readline_string()
        self.hashlenth()
        self.stringlenth()
        self.Calculate_ALLCorpus()

    def readline_hash(self):
        with open(r'D:\test111\PS2CPC-Launcher\en_us copy.txt', encoding='utf-8') as f:#此处的路径为绝对路径，请自行修改
            lines = f.readlines()
        step = len(lines)
        Hash_str = []
        for i in range(0,step):
            lines1 = lines[i].split()
            Hash = lines1[0]
            Hash_str.append(Hash)
            
        return Hash_str
    
    def readline_string(self):
        with open(r'D:\test111\PS2CPC-Launcher\en_us copy.txt', encoding='utf-8') as f:#此处的路径为绝对路径，请自行修改
            lines = f.readlines()
        step = len(lines)
        Corpus = []
        for i in range(0,step):
            lines1 = lines[i].split()
            Corpus_str = lines1[2:]
            Corpus.append(Corpus_str)
        
        return Corpus

    def hashlenth(self):
        lines = self.readline_hash()
        step = len(lines)
        Hash_lenth = []
        for i in range (0,step):
            H_lenth = len(lines[i])
            Hash_lenth.append(H_lenth)
        
        return Hash_lenth

    def stringlenth(self):
        lines = self.readline_string()
        step = len(lines)
        String_lenth = []
        lenth = 0
        for i in range(0,step):
            Point = len(lines[i])
            if Point == 1:
                lines1 = lines[i]
                S_lenth = len(lines1[0].encode('utf-8'))
                String_lenth.append(S_lenth)
            else:
                lines2 = lines[i]
                len1 = []
                for i in range(0,Point):
                    len1.append(len(lines2[i].encode('utf8')))
                lenth = sum(len1)
                lenth1 = lenth + (Point - 1)
                String_lenth.append(lenth1)

        return String_lenth

    def Calculate_ALLCorpus(self):
        Hash = self.hashlenth()
        String = self.stringlenth()
        Corpus_lenth = []
        step = len(Hash)
        for i in range (0,step):
            lenth = Hash[i] + String[i] + 6
            Corpus_lenth.append(lenth)
        
        return Corpus_lenth
    
    def Calculate_linkCorpus(self):
        Hash_lenth = self.hashlenth()
        Corpus_lenth = self.Calculate_ALLCorpus()
        step = len(Hash_lenth)
        Link_Corpus = [3]
        for i  in range (0,step):
            link = Link_Corpus[i] + Corpus_lenth[i] + 2
            Link_Corpus.append(link)
        return Link_Corpus


    def test(self):
        print(self.readline_hash())
        print(self.readline_string())
        print(self.hashlenth())
        print(self.stringlenth())
        print(self.Calculate_ALLCorpus())
        print(self.Calculate_linkCorpus())

class Generate(Length):

    def __init__(self):
        self.Generate_dir

    def Generate_dir(self):
        hash = self.readline_hash()
        link_lenth = self.Calculate_linkCorpus()
        corpus_lenth = self.Calculate_ALLCorpus()
        Generate_dir = []
        step = len(hash)
        for i in range(0, step):
            Out_str = str(hash[i]) + str('	') + str(link_lenth[i]) + str('	') + str(corpus_lenth[i]) + str('	d\n')
            Generate_dir.append(Out_str)
        
        return Generate_dir


class main(Generate,Length):

    def __init__(self):
        self.Create()

    def Create(self):
        dir = self.Generate_dir()
        step = len(dir)

        text = "## CidLength:	63\n## Count:	45598\n## Date:	Tue Jan 25 10:20:19 PST 2022\n## Game:	PSNXCN\n## Locale:	zh_CN\n## MD5Checksum:	B0B55E518C6C2FEC202963E3F7C11F61\n## T4Version:	2.1.0047\n## TextLength:	1594\n## Version:	2.1.1293249\n"
        f = open("test1.txt","a")
        f.write(str(text))
        f.close 
        for i in range(0,step):
            f = open("test1.txt","a")#此处会在文件所在目录自动生成test1.txt文件
            f.write(dir[i])
            f.close 
        print('完成')





    


    


Test = main()
