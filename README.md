# BruteForcer-For-XML-Request-Files-POC

This tool aims to bruteforce for saved response/requests in XML format(for example burp requests). As we know, Burpsuite, hydra, etc. programs may do it simply, but in burpsuite we can not use big files ( it is freezing) and sometimes (for example for the websites which require 2 authentications) we can not use hydra. But this tool is just in tests, so may not work.

Installation:

wget https://github.com/zer0da/BruteForcer-For-XML-Request-Files-POC.git

cd BruteForcer-For-XML-Request-Files-POC/

Usage Ex:

Intercept the request you want and then sent the request. Note, sending the request is important because the tool requires responses from the file.

![Screenshot_1](https://user-images.githubusercontent.com/65029938/151867546-a78be77b-f916-4c7f-8b9b-2add18f0960b.png)

Save it!

![Screenshot_2](https://user-images.githubusercontent.com/65029938/151867575-000ed9e9-7161-4666-b9bc-1cac193dc7d5.png)

Then run it with python3.

![Screenshot_4](https://user-images.githubusercontent.com/65029938/151867613-81e707e6-8878-4feb-8898-02deff64dac9.png)



