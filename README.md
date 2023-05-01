# Bytsho
Bytsho is a simple yet smart binary compression algorithm. 
___
# FAQ


## How does it work?
Bytsho reads the binary of a given file. It then replaces every `10` and `01` binary sequence into `1` and `0` until there are no more capable replacements to make. It also counts the replacements it has made so that we can uncompress the file later on. (Which works in a similar matter, by adding `10` `01` sequences for each `1` and `0` `* amount of replacements`

## Why isn't there a reverse process? 
Well, undoing the compressed algorithm would take a lot of memory and compuiting power to finish successfuly. I've tried a lot of decompression methods but they all overloaded my computer, so if you have a more lightweight method, then let me know!
