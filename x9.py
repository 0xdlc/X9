from urllib.parse import urlparse




class x9(object):
    def __init__(self,
                 url: str,
                 wordlist_path: str,
                 chunk: int) -> None:
        self.values = ("'voorivexinjected'","\"voorivexinjected\"","<b/voorivexinjected")
        self.url = url
        self.wl = wordlist_path
        self.chunk = chunk

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

    def ignore(self):
        params=[]
        parsed = urlparse(self.url)
        parsed2 = urlparse(parsed._replace(query="").geturl())
        _and = ""
        if parsed.query:
            _and = "&" #This is how bad i am as a programmer lol
        words = []
        with open(self.wl) as file:
            for chunk_number in range(1):
                for value in self.values:
                    for word in self.file_block(fp=file, number_of_blocks=1, block=chunk_number):
                        word = word.rstrip()
                        words.append(f"{word}={value}")
                        if len(words) == self.chunk:# or block.index(word)==block[-1]:
                            parsed2 = parsed._replace(query=f"{parsed.query}{_and}{'&'.join(words)}").geturl()
                            print(f"{parsed2}\n")
                            words=[]




        #if parsed.query:




            # while True:
            #     params.append(file.readline().rstrip())
                