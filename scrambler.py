from encrypt_or_decrypt import encrypt_caesar, encrypt_vizhener, encrypt_vernam
from hacker import hacker_func
import click


class Context:
    def __init__(self, input_filename, output_filename):
        with open(input_filename) as f:
            self.text = f.read()
        self.output_filename = output_filename

    def write(self, text):
        if self.output_filename is None:
            print(text)
        else:
            with open(self.output_filename, 'w') as f:
                f.write(text)


@click.group()
@click.argument('input_file', required=True)
@click.option('-o', 'output_file')
@click.pass_context
def cli(ctx, input_file, output_file=None):
    ctx.obj = Context(input_file, output_file)


@cli.command()
@click.option('--key', type=click.INT, required=True)
@click.option('--decrypt', '-d', is_flag=True)
@click.pass_obj
def caesar(ctx, key, decrypt=False):
    ctx.write(encrypt_caesar(ctx.text, key, decrypt=decrypt))


@cli.command()
@click.option('--key', required=True)
@click.option('--decrypt', '-d', is_flag=True)
@click.pass_obj
def vizhener(ctx, key, decrypt=False):
    if not all(sym.isalpha() for sym in key):
        print("key must contain only letters")
        return
    ctx.write(encrypt_vizhener(ctx.text, key, decrypt=decrypt))

@cli.command()
@click.option('--key', required=True)
@click.option('--decrypt', '-d', is_flag=True)
@click.pass_obj
def vernam(ctx, key, decrypt=False):
    if not all(sym.isalpha() for sym in key):
        print("key must contain only letters")
        return
    ctx.write(encrypt_vernam(ctx.text, key, decrypt=decrypt))


@cli.command()
@click.pass_obj
def broke(ctx):
    ctx.write(hacker_func(ctx.text))


if __name__ == '__main__':
    cli()