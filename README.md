# chatbotdesafio

A intenção foi desenvolver um código capaz de utilizar a API do Gemini através do próprio código.

Inicialmente foi criado um Ambiente virtual para separar as bibliotecas necessárias para o projeto;
Para a criação do ambiente, foi necessário acessar o terminal e utilizar o comando python -m venv (nome do Ambiente virtual);
Após a criação do ambiente, foi consultado o Quickstart do próprio Gemini, https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=pt-br#setup_your_api_key ;
Como não era a intenção desenvolver através de Notebooks Jupyter, só precisei atender os requisitos de versão do Python;
Logo, foi feita a instalação das bibliotecas necessárias para a importação dos comandos da API;
No terminal, dentro do venv (ambiente virtual) ativado, o comando pip install -U google-generativeai, foi utilizado, e então as importações e comandos relevantes para o objetivo do projeto foram utilizados;
Tendo feito isso, então, a próxima etapa consiste em gerar uma chave API para a utilização;
Através do passo a passo descrito em https://aistudio.google.com/app/apikey?hl=pt-br foi gerada a chave utilizada no código;
Outro fator levado em consideração foi a atenção à segurança dos dados no código, assim foi utilizado um arquivo .env para ocultar a chave API;
Novamente no terminal, foi utilizado o comando para o acesso às bibliotecas dotenv, pip install python-dotenv ;
Após isso, houveram as importações no código, e a utilização dos comandos para a utilização da biblioteca;
Um arquivo .env precisa ser criado, nele será armazenada a API seguindo o modelo "Variável=ChaveAPI";
É necessário seguir essa grafia, colocando no documento a variável correspondente à utilização da chave, e a chave retornada como valor da variável;
Tendo seguido esses passos, o código se mostrou funcional e eficiente, devolvendo diferentes resultados para diferentes interações com o Gemini.



