from docx2pdf import convert
from pathlib import Path

count=0
exclude=input('Exclusions(ex-note1,book,project): ')
output=input('Output path(default-same folder as docx files): ')
exclusions=[e + '.docx' for e in exclude.split(',')]
folder=Path(__file__).parent
for file in folder.glob('*.docx'):
    if file.name not in exclusions:
        if output==None:
            convert(file)
        else:
            convert(file,output + '\\' + file.stem + '.pdf')
        print(file.name + ' ✓')
        count+=1
print(str(count) + ' files converted!')