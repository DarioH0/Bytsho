# PROJECT CURRENTLY UNDER RECONSTRUCTION.
I'm currently re-building the project in Golang, making it *actually* work, improving performance, and fixing all of the issues.
<br/>
<br/>
<br/>
<br/>

## How does it work?
Bytsho reads the binary of a given file. It then replaces every `10` and `01` binary sequence into `1` and `0` until there are no more capable replacements to make. It also counts the replacements it has made so that we can uncompress the file later on. (Which works in a similar matter, by adding `10`, `01` sequences for each `1` and `0` `* amount of replacements`.

