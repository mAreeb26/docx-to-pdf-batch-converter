from docx2pdf import convert
from pathlib import Path

count=0
exclude=input('Exclusions(ex-note1,book,project): ')
exclusions=[e + '.docx' for e in exclude.split(',')]
folder=Path(__file__).parent
for file in folder.glob('*.docx'):
    if file.name not in exclusions:
        convert(file)
        print(file.name + ' ✓')
        count+=1
print(str(count) + ' files converted!')