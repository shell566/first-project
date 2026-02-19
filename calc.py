#!/usr/bin/env python3

from rich.console import Console
from rich.text import Text

console = Console()

a = """              .__                     __                .__   
  ____ _____  |  |   ____           _/  |_  ____   ____ |  |  
_/ ___\\__  \ |  | _/ ___\   ______ \   __\/  _ \ /  _ \|  |  
\  \___ / __ \|  |_\  \___  /_____/  |  | (  <_> |  <_> )  |__
 \___  >____  /____/\___  >          |__|  \____/ \____/|____/
     \/     \/          \/                                    """

text = Text(a)
text.stylize("bold cyan")  # لون عام للشعار كله

console.print(text)
console.print("[bold yellow]----------- calc-tool -----------[/bold yellow]")

x = float(console.input("[green]Enter the first number:[/green] "))
y = float(console.input("[green]Enter the second number:[/green] "))
op = console.input("[magenta]Enter the operation (+, -, /, *):[/magenta] ")

if op == "+":
    console.print(f"[bold blue]Result:[/bold blue] {x + y}")
elif op == "-":
    console.print(f"[bold blue]Result:[/bold blue] {x - y}")
elif op == "/":
    if y != 0:
        console.print(f"[bold blue]Result:[/bold blue] {x / y}")
    else:
        console.print("[bold red]Error: Division by zero[/bold red]")
elif op == "*":
    console.print(f"[bold blue]Result:[/bold blue] {x * y}")
else:
    console.print("[bold red]Error: Invalid operation[/bold red]")
