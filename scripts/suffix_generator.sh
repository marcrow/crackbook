#!/bin/bash

output='./05-custom-suffix.rule'
# Special character set used 
special='/*-+!:;.,??$=<#@'

# Do not remove this line
echo ":" > $output

echo '### Single digit - $?d' >> $output
mp64 \$?d >> $output

echo '### Double digit - $?d $?d' >> $output
mp64 \$?d\$?d >> $output

echo '### Single symbol - -1 "/*-+!:;.,??$=<#@" \$?1' >> $output
mp64 --custom-charset1="$special" \$?1 >> $output 

echo '### Single symbol + single digit - $?s $?d' >> $output
mp64 --custom-charset1=$special \$?1\$?d >> $output 

echo '### Single symbol + double digit - $?s $?d $?d' >> $output
mp64 --custom-charset1=$special \$?1\$?d\$?d >> $output 

echo '### Year (1900-1999) - $1 $9 $?d $?d' >> $output
mp64 \$1\$9\$?d\$?d >> $output

echo '### Year (2000-2029) - $2 $0 $?1 $?d' >> $output
mp64 \$2\$0\$?d\$?d >> $output

echo '### Single symbol + year (1900-1999) - $?s $1 $9 $?d $?d' >> $output
mp64 --custom-charset1=$special \$?1\$1\$9\$?d\$?d >> $output

echo '### Single symbol + year (2000-2029) - $?s $2 $0 $?1 $?d' >> $output
mp64 --custom-charset1=$special \$?1\$2\$0\$?d\$?d >> $output

echo '### year (1900-1999) + single symbol' >> $output
mp64 --custom-charset1=$special \$1\$9\$?d\$?d\$?1 >> $output

echo '### year (2000-2029) + single symbol' >> $output
mp64 --custom-charset1=$special \$2\$0\$?d\$?d\$?1 >> $output



echo '### Double digit + single symbol - $?d $?d $?s' >> $output
mp64 --custom-charset1=$special \$?d\$?d\$?1 >> $output 


echo '### 123 suffix' >> $output
mp64 \$1\$2\$3 >> $output 

echo '### 0123 suffix' >> $output
mp64 \$0\$1\$2\$3 >> $output 

echo '### <3 and :) and (: suffix' >> $output
mp64 \$\<\$3 >> $output 
mp64 \$:\$\) >> $output 

