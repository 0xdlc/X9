from urllib.parse import urlparse
import subprocess
import os



class x9(object):
    def __init__(self,
                 wordlist_path: str,
                 chunk: int,
                 tempfile: str = "/tmp/tmp_wl.txt",
                 template:str = "utils/xxs_template.yaml",
                 temp_chunk: int = 1000) -> None:
        self.values = ("'testinquiz'","\"testinquiz\"","<b/testinquiz")
        self.template = template
        self.wl = wordlist_path
        self.chunk = chunk
        self.tempfile = tempfile
        self.temp_chunk = temp_chunk


    def nuclei(self):
        with open(self.tempfile,'r') as file:
            cwd = os.getcwd()
            self.template = os.path.join(os.getcwd(),self.template)
            _list = os.path.join(cwd,self.tempfile)
            subprocess.check_output(["./nuclear.sh",_list,os.path.expanduser(self.template)],text=True)#.stdout.decode('utf-8')


    def file_block(self,fp, number_of_blocks, block):

        assert 0 <= block and block < number_of_blocks
        assert 0 < number_of_blocks
    
        fp.seek(0,2)
        file_size = fp.tell()
    
        ini = file_size * block / number_of_blocks
        end = file_size * (1 + block) / number_of_blocks
    
        if ini <= 0:
            fp.seek(0)
        else:
            fp.seek(ini-1)
            fp.readline()
    
        while fp.tell() < end:
            yield fp.readline()


    def combine(self,url: str):
        parsed = urlparse(url)
        _and = ""
        if parsed.query:
            _and = "&" #This is how bad i am as a programmer lol
        words = []
        urls = []

        with open(self.wl) as file:
            for chunk_number in range(self.chunk):

                for value in self.values:
                    for word in self.file_block(fp=file, number_of_blocks=self.chunk, block=chunk_number):
                        word = word.rstrip()
                        words.append(f"{word}={value}")

                        if len(words) == self.chunk:# or block.index(word)==block[-1]:
                            parsed2 = parsed._replace(query=f"{parsed.query}{_and}{'&'.join(words)}").geturl()
                            urls.append(parsed2)

                            if len(urls) == self.temp_chunk:
                                with open(self.tempfile,"w") as temp_file:
                                    for i in urls:
                                        temp_file.write(i+"\n")
                                self.nuclei()

                                urls=[]
                            words=[]


    def replace(self,url: str):
        parsed = urlparse(url)
        queries = parsed.query.split("&")
        url_params,urls,words = [],[],[]

        for i in queries:
            url_params.append(i.split("=")[0])
        words_len = len(url_params)

        _and = "&"

        with open(self.wl) as file:
            for chunk_number in range(self.chunk):

                for value in self.values:
                    words=[]
                    for i in url_params:
                        words.append(f"{i}={value}")
                    for word in self.file_block(fp=file, number_of_blocks=self.chunk, block=chunk_number):
                        word = word.rstrip()
                        words.append(f"{word}={value}")

                        if len(words) >= self.chunk:# or block.index(word)==block[-1]:
                            parsed2 = parsed._replace(query=f"{'&'.join(words)}").geturl()
                            urls.append(parsed2)

                            if len(urls) >= self.temp_chunk:
                                with open(self.tempfile,"w") as temp_file:
                                    for i in urls:
                                        temp_file.write(i+"\n")
                                self.nuclei()
                                urls=[]
                            words=words[0:words_len]      

        #if parsed.query:




            # while True:
            #     params.append(file.readline().rstrip())
                
