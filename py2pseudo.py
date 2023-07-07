class Translator:

    last_op = '' # last operator used (if, for, while, ...)
    last_op_count = 0 # last indentation
    
    def main(self,pycode):
        with open(pycode, 'r') as code:
            latexpseudo = code.readlines()
            print(latexpseudo)
            translated = ''
            for i in latexpseudo[1:]:
                if i.replace(" ","")[0:2] == 'if':
                    translated += self.translate_if(i)
                elif i.replace(" ","")[0:2] == 'wh':
                    translated += self.translate_while(i)
                else:
                    translated += self.translate_simple_chunk(i)
            print(translated)
            return translated

    def translate_simple_chunk(self,chunk):
        count = self.count_spaces(chunk)
        trnchunk = ''
        if count < self.last_op_count and self.last_op != '':
            if self.last_op == 'if':
                trnchunk += '\n\EndIf'
                self.last_op_count = 0
                self.last_op = ''
            if self.last_op == 'while':
                trnchunk += '\n\EndWhile'
                self.last_op_count = 0
                self.last_op = ''
        if '=' in chunk:
            i = chunk.index('=')
            trnchunk +=  '\n\State ' + "$ " + chunk[0:i].replace(" ","") + "\gets" + chunk[i+1:] + " $"
            
            return trnchunk
        return trnchunk
            
    def translate_if(self,chunk):
        self.last_op_count = self.count_spaces(chunk) + 4
        self.last_op = 'if'
        chunk = chunk.replace(" ","")
        chunk = chunk.replace(":","")
        trnchunk = '\n\If'
        trnchunk +=  '{' + f'${chunk[2:-1]}$' + '}'
        return trnchunk
    
    def translate_while(self,chunk):
        self.last_op_count = self.count_spaces(chunk) + 4
        self.last_op = 'while'
        chunk = chunk.replace(" ","")
        chunk = chunk.replace(":","")
        trnchunk = '\n\While'
        trnchunk +=  '{' + f'${chunk[5:-1]}$' + '}'
        return trnchunk
    
    def count_spaces(self,chunk):
        count = 0
        for i in chunk:
            if i == ' ':
                count +=1
            else:
                return count
        return count


trans = Translator()
trans.main("ex.py")
