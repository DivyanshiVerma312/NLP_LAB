import asyncio
import sys
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import nbformat
from nbclient import NotebookClient

print("Reading GPT2Model.ipynb...")
nb = nbformat.read('GPT2Model.ipynb', as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name='python3')
print("Executing notebook cells...")
client.execute()

nbformat.write(nb, 'GPT2Model.ipynb')
print("Successfully executed all cells and updated GPT2Model.ipynb!")
