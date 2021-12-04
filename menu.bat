@echo off
cd N:\Przedmiotowe_pliki\Jezykiskryptowe\Projekt
:menu
cls
echo  _______________________________Menu________________________________
echo.                                                                       
echo  Wybierz jedna z ponizszych opcji                                  
echo  Wyboru mozesz dokonac wprowadzajac odpowiedni numer z klawiatury  
echo  1. Start progarmu                                                 
echo  2. Backup                                                         
echo  3. Informacje o programie  
echo  4. Wyniki programu                                        
echo  5. Zamknij program                                                                                             
echo ___________________________________________________________________
echo.
set /p choice="Wybor (1/2/3/4/5): "

IF %choice%==1 GOTO first
IF %choice%==2 GOTO second
IF %choice%==3 GOTO third
IF %choice%==4 GOTO fourth
IF %choice%==5 GOTO fifth

echo.
echo Nie ma takiej opcji, sprobuj ponownie!
pause
GOTO :menu

:first
cls
call program.py
pause
GOTO :menu


:second
cls
mkdir C:\Users\user\Desktop\%date%
copy N:\Przedmiotowe_pliki\Jezykiskryptowe\Projekt C:\Users\user\Desktop\%date%
echo Kopia zapasowa zostala wykonana pomyslnie
pause
GOTO :menu


:third
cls
echo.
echo ____________________________________________________________________________________________________
echo.
echo Ogolne dzialanie programu:
echo.
echo Dzialanie programu opiera sie na trzech zegarach, posrod ktorych kazdy dziala inaczej
echo.
echo Wyobrazmy sobie nastepujaca sytuacje:
echo  # pierwszy zegar spoznia o 5 sekund
echo  # drugi zegar przyspiesza o 5 sekund
echo  # trzeci zegar dziala poprawnie
echo.
echo Zadaniem tego programu jest obliczenie czasu, ktory uplynie az dane trzy zegary sie spotkaja
echo.
echo ____________________________________________________________________________________________________
echo.
echo Dane wejsciowe:
echo  # zapisane sa w pliku daneWejsciowe.txt
echo  # format: 
echo             "zegar1||zegar2||zegar3/n"
echo             "zegar1||zegar2||zegar3/n"
echo             itd.
echo      Przy czym pod wartoscia zegar1/zegar2/zegar3 kryja sie informacje o danym zegarze w formacie:
echo       # "H:M|-wartosc_opoznienia/+wartosc_przyspieszenia"
echo       # w przypadku kiedy zegar dziala poprawnie nalezy wpisac "0"
echo.
echo      Dla przykladu:
echo       # "14:30|+5||16:30|-5||15:30|0"
echo       # zegar1 przyspiesza 5 sekund
echo       # zegar2 opoznia 5 sekund
echo       # zegar3 dziala poprawnie
echo.
echo ____________________________________________________________________________________________________
echo.
echo Dane wyjsciowe:
echo # zapisane sa w pliku daneWyjsciowe.txt
echo # wynik reprezentujacy czas, ktory minal jest podany w sekundach
echo. 
pause
GOTO :menu

:fourth
cls
start index.htm
GOTO :menu

:fifth
exit
