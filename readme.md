# Find Extensions - Parse and Extract Unique Extensions
While performaing site assessments, we may encounter situations where we need to find extensions that are not accounted in the caching rules. Using this python program, the list of extensions can be extracted.

## Usage
Simply run the command on terminal and pass the file containing list of urls with the `--file` option. The list of URLs can either be a plain-text file or it can be a gzip compressed file.

```bash
usage: find_extension.py [-h] --file FILE

Print extension from a set of URLs/ARLs

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  File containing list of URLs/ARLs
```

## What's special?
Initially, I'd built this using the python's _split_ function. The logic worked as follows:

- Extract URL
- Split the string at '?' if present. This will give the URL and query parameters. Ignore the query params.
- Now, split the string to extract the string after the last '/'. I'd used __rsplit__ function for this. We now have the file name.
- Take the file name and run a __rsplit__ again to get the extension.

This solution worked but it felt very combersome. Before each split, I had to use a _.find()_ to ensure the right characters were present.

As a work-around this I used a direct regex method.

### Regex based solution
In the regex based solution, I rely on the _greedy_ match that python uses by default. The logic runs as follows:

- Take the string and match everything until the last '/' followed by something until the '.' character. This is a non-capturing regex since we don't really need this bit for our analysis. This is the regex `(?:[^\?]+\.)`.
- With the string that is left, extract anything that is a character or a number. This is a capturing regex and will be captured as the first group. This part is represented by the regex `([a-zA-Z0-9]+)`.
- Finally, we need to ensure that the part following the extension characters is either a _?_ or the end of string _$_. That's represented by the regex `(?:$|\?)`.

Thus, a single regex with no further checks does the multi-stage/multi-check work provided by out of box libraries.

Hope you find it useful!

