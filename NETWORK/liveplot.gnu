set datafile separator ","
set autoscale
set xlabel "Time"
set ylabel "Speed"
set style data histogram
set style histogram clustered
set style fill transparent solid border 1.0
set boxwidth 0.8 relative
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "#808080" behind

plot for [COL=2:3] 'bandwidthdata.csv' using COL:xticlabels(1) title columnheader
pause 1 
reread
