@echo off
title dc checkker Kutuphane Yukleyici
echo Kutuphaneler indiriliyor, sabret orospu cocugu!
echo Python pip guncelleniyor...
python -m ensurepip --upgrade
python -m pip install --upgrade pip
echo Requests kutuphanesi yukleniyor...
python3.13 -m pip install requests --user
echo PySocks kutuphanesi yukleniyor...
python3.13 -m pip3 install pysocks --user
echo Stem kutuphanesi yukleniyor...
python3.13 -m pip3 install stem --user
echo Bitti, artik hacklemeye hazirsin, serefsiz!
pause
