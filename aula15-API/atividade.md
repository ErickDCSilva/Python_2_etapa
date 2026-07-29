PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Bonecas Falantes","autor":"Enzo","ano":1967}'


ano          : 1967
autor        : Enzo
data_criacao : 2026-07-29 09:04:54.791649
id           : 4
titulo       : Bonecas Falantes



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3B1","ano":2026}'


ano          : 2026
autor        : 3B1
data_criacao : 2026-07-29 09:01:48.359720
id           : 1
titulo       : Cotemig



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Último Acorde em Viena","autor":"Arthur m. Valente","ano":2021}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xda in position 13: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Último Acorde em Viena","autor":"Arthur m. Valente","ano":2021}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xda in position 13: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Último","autor":"Arthur","ano":2021}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xda in position 13: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Último","autor":"Arthur","ano":2021}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xda in position 11: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12401188>   Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Viena","autor":"arthur","ano":2021}'


ano          : 2021
autor        : arthur
data_criacao : 2026-07-29 09:28:43.153823
id           : 5
titulo       : Viena



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo": "Ecos", "autor": "Elena", "ano": 2024}'


ano          : 2024
autor        : Elena
data_criacao : 2026-07-29 09:34:06.147149
id           : 6
titulo       : Ecos



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo": "O Segredo", "autor": "Clara", "ano": 2019}'


ano          : 2019
autor        : Clara
data_criacao : 2026-07-29 09:34:46.402536
id           : 7
titulo       : O Segredo



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo": "Algoritmos", "autor": "Lucas", "ano": 2025}'


ano          : 2025
autor        : Lucas
data_criacao : 2026-07-29 09:35:21.930019
id           : 8
titulo       : Algoritmos



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo": "A Filha", "autor": "Samuel", "ano": 2022}'


ano          : 2022
autor        : Samuel
data_criacao : 2026-07-29 09:35:54.387914
id           : 9
titulo       : A Filha



PS C:\Users\12401188>   Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo": "Rastros", "autor": "Diana", "ano": 2026}'


ano          : 2026
autor        : Diana
data_criacao : 2026-07-29 09:36:59.267001
id           : 10
titulo       : Rastros



PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE

PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE

PS C:\Users\12401188> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE
