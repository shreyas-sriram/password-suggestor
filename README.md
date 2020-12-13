# password-suggestor
*Long, simple, easy-to-remember passphrases* > *short, complex, difficult-to-remember passwords*. Like *xkcd* has said it [here](https://xkcd.com/936/).
	
Example : **boat-plant-lift-trick** is better to remember than **[>oh187no;'0+**.

**Note : If quantum computers have been established commercially, this tool is obsolete!**:no_entry:

**Note : Passwords are not saved anywhere, the entire code runs in the browser. Turn off the internet connection before trying it out!**:v:

## Usage
* The generated suggestions are made of 4 words separated by a separator.
	* Two words are entered by the user.
	* The third word is chosen at random from the list.
	* Fourth word is an abbreviated form of a proverb chosen by the user.

* Suggested passwords include trivial substitutions to characters (**a** becomes **@**, **s** becomes **$**).
 Although trivial substitutions do not make a password actually stronger, it helps when websites required a combination of **Upper case, lower case, special characters and number**.
 Three passwords are suggested to satisfy the website requirements for password complexity.

* Example :
	* word 1 - hello
	* word 2 - world
	* word 3 - item (chosen at random from the list)
	* word 4 - npng (derived from **no pain, no gain**)
	* Suggestions :
		* hello-npng-world-item
		* heLlo-npng-world-item
		* heLlo-npng-world-it3m


### Acknowledgements
List of words from [EFF Long Wordlist](https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt).

List of proverbs from [1000 ENGLISH PROVERBS](https://suratiundhiyu.files.wordpress.com/2011/02/1000-english-proverbs.pdf).

Password strength evaluation by [zxcvbn](https://github.com/dropbox/zxcvbn).

Motivation from humans' incapacity to make strong passwords and the greatest comic [xkcd](https://xkcd.com/936/)!:fire::clap:
