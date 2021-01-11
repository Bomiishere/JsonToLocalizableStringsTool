# JsonToLocalizableStringsTool

#### Features

- generate Localizable.strings to target directory in ios project

#### Requirements

* Python 3
* pip install

#### Modules
| Json  | Rex  | Date
| :---: |:---------------:|:----:|
| json | re | datetime

### Usage
##### Required
###### 1. Edit Setup in xlsx_convert.py 
```
# 讀取檔案
source_directory: generated json from backend dir

# 目標檔案
project_directory: iOS project dir

###### 2. Execute convert_xlsx.py, generate Localizable.strings
```
python3 xlsx_convert.py
```
##### Optional
###### 修改 output file 註解
```
header_1_export_file_name = 'Localizable' + '-' + language.value + '.strings'
header_2_from_where = 'from Backend_CaiLiFang.Locale.Resx' 
header_3_created_by = 'auto generated'
header_4_create_date = datetime.datetime.now().strftime('%Y/%-m/%-d')
header_5_create_year = datetime.datetime.now().strftime('%Y')
header_6_copyright = 'JohnsonTechInc.'
```

#### Tips
* python3 install, [click me for reference](https://stringpiggy.hpd.io/mac-osx-python3-dual-install/)

* install modules
```bash
python3 -m pip install --upgrade xlsxwriter
```

* install jupyter
```
pip3 install jupyter
```
