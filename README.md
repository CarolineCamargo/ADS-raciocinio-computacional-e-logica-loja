# Este é um projeto entregue na Atividade Prática (ATP) da disciplina de Raciocínio Computacional e Lógica no início da minha graduação em Análise e Desenvolvimento de Sistemas no ano de 2020.

## Descrição de atividades:
### ATIVIDADE PRÁTICA (ATP): Etapa 1
#### Para esta etapa, faça um algoritmo que atenda às seguintes instruções:
##### A - Mostre ao usuário o seu nome completo, junto do nome da sua loja (não peça ao usuário o nome dele, apenas o mostre).
Exemplo: se o seu nome for João Flores da Silva, pode mostrar “Bem-vindo à Loja do João Flores da Silva” ou “Esta é a Loja Desconto da Cidade, bem-vindo! Aqui quem fala é João Flores da Silva”.
##### B - Diga ao usuário que fará uma análise de crédito dele. Para tal, peça que digite o cargo na empresa em que trabalha atualmente, o salário e o ano de nascimento.
##### C - Mostre ao usuário o cargo, o salário e o ano de nascimento que digitou.

### ATIVIDADE PRÁTICA (ATP): Etapa 2
#### Agora, vamos fazer uma análise de crédito do usuário para saber quanto ele poderá comprar na nossa loja. Assim, continue do ponto em que parou na etapa 1 e, usando o mesmo código, adicione os seguintes passos:
##### A - Mostre na tela a idade aproximada do usuário. Você pode fazer isso ao subtrair o ano em que estamos pelo ano de nascimento que ele digitou.
##### B - Mostre quanto o cliente poderá gastar na sua loja (o limite de gasto), calculado da seguinte forma: [salário x (idade / 1.000)] + 100.

### ATIVIDADE PRÁTICA (ATP): Etapa 3
#### Agora, vamos verificar se o produto que solicitamos ao usuário pode ser realmente comprado por ele (ou não). Aqui, vamos usar o seu nome completo para montar a lógica.
#### Atenção! Vamos usar como lógica o seu nome completo e não o nome do usuário. A partir de agora, quando falarmos “quantidade de caracteres do seu primeiro nome”, equivale à quantidade de letras do seu primeiro nome. Por exemplo, se o seu nome completo é João Flores da Silva, isso seria igual a quatro. Quando falarmos “quantidade de caracteres do seu nome completo”, contaremos também espaços e hifens. No mesmo exemplo, seria igual a 20.
##### A - Solicite ao cliente que digite o nome de um produto e o preço dele.
##### B - Se o valor do produto for menor ou igual a 60% do limite que o cliente tem para gastar, mostre a mensagem “Liberado!”. Se estiver entre 60% e 90%, mostre a mensagem “Liberado ao parcelar em até 2 vezes”. Se estiver entre 90% e 100%, mostre a mensagem “Liberado ao parcelar em 3 ou mais vezes”. Caso contrário, mostre a mensagem “Bloqueado”.
##### C - Se o valor do produto estiver entre a quantidade de caracteres do seu nome completo e a idade do cliente, mostre que ele terá um desconto igual à quantidade de caracteres do seu primeiro nome.
##### D - Mostre também ao cliente o valor do produto com o desconto.

### ATIVIDADE PRÁTICA (ATP): Etapa 4
#### Vamos garantir que o nosso código possa funcionar para vários produtos? Para tanto, vamos modularizá-lo (isto é, criar funções) para eles, em conjunto com estruturas de repetição como for e while.
#### Execute os seguintes passos:
##### A - Coloque o código que você fez nas etapas 1 e 2 dentro de uma única função chamada “obter_limite”. Essa função deverá retornar o limite que o usuário poderá gastar.
##### B - Coloque o código que você fez na etapa 3 dentro de uma única função chamada “verificar_produto”. Essa função terá como parâmetro de entrada o limite de gasto do cliente.
##### C - Após o cliente informar os dados dele (pela função “obter_limite”), armazene o limite que ele poderá gastar dentro de uma variável chamada “limite”.
##### D - Na sequência, pergunte ao usuário quantos produtos deseja cadastrar.
##### E - Por fim, utilize uma estrutura de repetição (for ou while) por n vezes, com n equivalendo à quantidade de produtos que ele deseja cadastrar.
##### F - Dentro da sua estrutura de repetição, chame sua função “verificar_produto”, permitindo que o usuário consiga cadastrar todos os produtos e verificar se teria ou não limite sobrando para comprá-los.


