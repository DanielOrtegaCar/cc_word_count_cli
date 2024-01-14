# from funciones import count
import click
import sys
from typing import Tuple, IO, List, Union, TypeAlias

result_type: TypeAlias = Tuple[str, str, str, str, str]


def count(text_data: IO[bytes]) -> result_type:
    """
    count : Count bytes, words, characters of text data

    Args:
        text_data (IO[bytes]): text to count elements

    Returns:
        Tuple[str,str,str,str,str]: return bytes,chars, words, and lines like ints
    """

    byte_count = char_count = word_count = newlines = 0
    max_line_len = -9999

    for line in text_data:
        if max_line_len < len(line):
            max_line_len = len(line)
        byte_count += len(line)
        word_count += len(line.split())
        char_count += len(line.decode())

        if line.decode().endswith("\n"):
            newlines += 1

    return (
        str(newlines),
        str(word_count),
        str(char_count),
        str(byte_count),
        str(max_line_len),
    )


def get_result(
    filename: str, result: result_type, count_bytes: bool, count_lines: bool
) -> str:
    """
    get_result _summary_

    function to generate the result string, given the parameters

    Args:
        filename (str): _description_
        result (tuple): _description_
        count_bytes (bool): _description_
        count_lines (bool): _description_

    Returns:
        str: _description_
    """
    newlines, word_count, char_count, byte_count, max_line_len = result

    text = ""

    if count_lines:
        text = text + " {} ".format(newlines)

    if count_bytes:
        text = text + " {} ".format(byte_count)

    # como manejar el caso por default (?), que deberia mostrar todos
    else:
        text = text + " ".join(result)
    # agregamos el nombre del archivo al final
    text = text + " {}".format(filename)
    return text


def word_count(files: Union[str, List[str]], count_bytes: bool, count_lines: bool):
    # newline,  word, and byte

    # newline, word,  character,  byte,  maximum line length
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

        nuevo_resultado = get_result(filename, result, count_bytes, count_lines)
        # print(result)

        click.echo(nuevo_resultado)


@click.command()
@click.argument("files", nargs=-1, type=click.Path(exists=True))
@click.option(
    "-c",
    "--bytes",
    "count_bytes",
    is_flag=True,
    help="The number of bytes in each input file is written to the standard output.",
)
@click.option(
    "-l",
    "--lines",
    "count_lines",
    is_flag=True,
    help="The number of lines in the file.",
)
def cli(files, count_bytes, count_lines):
    print(files, count_bytes, count_lines)
    word_count(files, count_bytes, count_lines)


if __name__ == "__main__":
    cli()