# from funciones import count
import click
import sys
from typing import Tuple,IO,List,Union


def count(text_data:IO[bytes])->Tuple[str,str,str,str,str]:
    """
    count : Count bytes, words, characters of text data


    Args:
        text_data (str): text to count elements

    Returns:
        Tuple[str,str,str,str,str]: return bytes,chars, words, and lines like ints
    """

    byte_count = char_count = word_count = newlines = 0
    max_line_len = -9999

    for line in text_data:
        # print(line)
        if max_line_len< len(line): 
            max_line_len = len(line)

        byte_count += len(line)
        word_count += len(line.split())
        char_count += len(line.decode() )
        newlines += 1

    return str(newlines), str(word_count), str(char_count), str(byte_count),str(max_line_len)
    

def get_result(filename:str,result:tuple,count_bytes:bool)->str:
    newlines, word_count, char_count, byte_count,max_line_len = result
    
    

    text = ""
    if count_bytes:
        text = text + " {} ".format(byte_count)

    else:
        text = text + " ".join(result)
    # agregamos el nombre del archivo al final
    text = text + " {}".format(filename)
    return text



def word_count(files:Union[str,List[str]], count_bytes:bool):

    #newline,  word, and byte 
    
    #newline, word,  character,  byte,  maximum line length
    if not files:
        filename = ""
        files = ["-"]

    for file in files:
        filename = file

        if file == "-":
            result = count(text_data=sys.stdin.buffer)
        else:
            with open(file, "rb") as file_data:
                result = count(text_data=file_data)

        

        result = get_result(filename,result,count_bytes)
        # print(result)
 
        click.echo(result)


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-c",
    "--bytes",
    "count_bytes",
    is_flag=True,
    help="The number of bytes in each input file is written to the standard output."
)
def cli(files,count_bytes):
    print(files,count_bytes)
    word_count(files,count_bytes)


if __name__ == "__main__":
    cli()