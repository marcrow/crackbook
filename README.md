# Crackbook

Knowledge, resources and scripts for password cracking.

<img src="./img/crackbook-logo.png" width="500">


## Resources 

https://github.com/stealthsploit/OneRuleToRuleThemStill.git better rule list than OneRuleToRuleTfhemAll
https://github.com/StayPirate/Single-Seed-Wordlist-Generator/tree/master To create custom rule set

# Quickwin

## Offline hash cracking

### Rockyou & OneRuleToRuleThemStill
From my experience rockyou + OneRuleToRuleThemStill is globally pretty efficient.
```bash
hashcat -m 1000  nt_hashes.txt ../rockyou.txt -r ../OneRuleToRuleThemStill/OneRuleToRuleThemStill.rule --force -O 
```


### Custom Wordlist
Generate a custom wordlist using the following element:

- usernames,
- names,
- surnames,
- compagny name
- town

Then add some common based password
- admin_compagny_name
- guest

If you use copy/paste to generates it, i recommend to use the script [wordlist_beautifier](scripts/wordlist_beautifier.py).

# Try harder

If the rockyou and the OneRule mask doesn't provide the password you expected, you have to try harder.

You can focus on a single word and use custom mask. (Limited results)
You can reuse your previous custom worlist, and use custom mask to improve password cover. 

### Generate custom wordlist based on a single word

```bash
echo <Your_Word> | hashcat -r ../Custom_wordlist/02-case_toggle.rule -r ../Custom_wordlist/03-l33t/l33t_micro_1234.rule -r ../Custom_wordlist/04-prefix.rule -r ../Custom_wordlist/05-custom-suffix.rule -r ../Custom_wordlist/06-case-toggle-multiple-words.rule --stdout | sort -u > <Output.txt>
```


### Generate custom wordlist from wordlist on the fly for hashcat

I do not recommend to generate wordlist on the disk if you have to crack hash offline. As Hashcat generates in memory wordlist it is more efficient to directly test hash, than write it on the disk and then test it.

```bash
hashcat -m 1000  <File_with_hashes>  <Your_Wordlist> -r -r ../Custom_wordlist/02-case_toggle.rule -r ../Custom_wordlist/03-l33t/l33t_micro_1234.rule -r ../Custom_wordlist/04-prefix.rule -r ../Custom_wordlist/05-custom-suffix.rule -r ../Custom_wordlist/06-case-toggle-multiple-words.rule --force -O 
```

### Generate your own rule list
In the script folder i create a simple bash script to generate suffix rule list. Edit it to create your own. I used a custom special char worlist.