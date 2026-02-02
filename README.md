# ML-QBlackHole

Um repositório focado em manter o código utilizado para o estudo de ataques de Quantum Black Hole em redes quânticas simuladas pelo _framework opersource_ [SeQUeNCe](https://github.com/sequence-toolbox/SeQUeNCe). Esse repositório visa o melhor entendimente de como técnicar de ML (_Machine Learn_) se saem da detecção do ataque estudado e quais são os cenário mais favoráveis para a sua identificação utilizando de métricas de performance dos modelos provindos do _framework python_ [Scikit-learn](https://scikit-learn.org).

## Dependências

Para a utilização do código é necessário cumprir as seguintes dependências:

- `python >= 3.12`

## Uso

Após satisfazer as [dependências](#dependências), é necessário abrir o terminal para seguir os seguintes passos de configuração:

### Clonagem do repositório e Dependências

Para a clonagem do repositório é necessário utilizar a interface de comando do seu sistema. Ex: powershell, cmd, bash ou qualquer outro da sua preferência. Digite o seguinte comando para a clonagem do repositório:

```bash
git clone https://github.com/Arthur-Negrao-Smith/ML-QBlackHole.git
```

Agora é necessário entrar no repositório clonado com o comando `cd`.

```bash
cd ML-QBlackHole
```

Após esse comando, o diretório atual será o do projeto e será necessário instalar as dependências que estão dentro do `pyproject.toml`. Crie um ambiente virtual python para isso, utilize o da sua preferência: venv (nativa do python), conda, virtualenv ou qualquer outra. Para fins didáticos e de facilitação, utilizaremos o `python venv` para isso (verifique o pacote para o seu sistema). Utilizando o seguinte comando criaremos o ambiente virtual:

```bash
python -m venv .venv
```

Após esse passo, temos de ativar a nossa `venv` que pode variar de sistema para sistema e de shell para shell. Desse modo, iremos considerar o processo para um sistema _Linux_ genérico:

```bash
source .venv/bin/activate               # caso utilize windows, use: .\.venv\Scripts\activate.bat 
```

Agora seu ambiente atual está isolado dos externos e não haverá mais mistura na instalação de pacotes. Portanto, já é possível rodar o comando para instalar as dependências python:

```bash
pip install .
```

### Uso do _Jupyter notebook_

Como forma de facilitar o desenvolvimento e a leitura dos arquivos, optou-se pela utilização de _jupyter notebooks_. O código python está contido dentro do diretório `src/` do projeto e lá o _notebook_ `default_simulations_ml.ipynb` contem o código responsável pela geração dos dados coletados do processo de _Machine Learn_. Rode com a interface _jupyter like_ da sua preferência. Basta que rode o programa com o _jupyter kernel_ que está dentro da `.venv`. Para fins didáticos, utilizaremos o próprio _jupyter lab_ que foi instalado com os pacoter nos passos anteriores:

```bash
jupyter lab
```

**Importante:** Dentro de [artefatos](#artefatos) está contido o link do drive para o _dataset_ utilizado para o script funcionar. Por questões de limitação da plataforma _GitHub_, não foi possível enviar o arquivo para esse repositório por ser pesado demais. Logo, é necessário a instalação do arquivo do _dataset_ e move-lo para dentro `src/data/raw` com o nome de `default_simulation.csv`.

Dentro do _jupyter lab_ é necessário encontrar o arquivo `default_simulations_ml.ipynb`, nele está contido o código principal do trabalho. Clique no arquivo e depois em "Restart the kernel and run all cells" que possui o símbolo `⏩`.

## Artefatos

- [Dataset utilizado](https://drive.google.com/file/d/1UXbmwkoH_ewnbYrjmwbx-MA3c38hd9eD/view?usp=sharing)

## Autores

- Arthur Negrão Smith
- Diego Abreu
