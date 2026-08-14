from docx2pdf import convert
from pathlib import Path

count=0
intake=input('Type in folder path(default-same folder which the .py file is saved in): ')
exclude=input('Exclusions(type in exact file name without the extension): ')
output=input('Output path(default-same folder as docx files): ')
exclusions=[e + '.docx' for e in exclude.split(',')]
if intake=='':
    folder=Path(__file__).parent
else:
    folder=Path(intake)
for file in folder.glob('*.docx'):
    if file.name not in exclusions or exclusions==None:
        if output=='':
            convert(file)
        else:
            convert(file,output + '\\' + file.stem + '.pdf')
        print(file.name + ' ✓')
        count+=1
print(str(count) + ' files converted!')