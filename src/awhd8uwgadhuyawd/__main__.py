import click

from awhd8uwgadhuyawd import fib, b_func


@click.command()
@click.argument("n", type=int)
def main(n: int):
    b_func(10)
    print(fib(n))


if __name__ == "__main__":
    main()
