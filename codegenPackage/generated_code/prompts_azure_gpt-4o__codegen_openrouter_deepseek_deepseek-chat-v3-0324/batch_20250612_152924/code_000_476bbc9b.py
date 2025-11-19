"""
Generated Code Metadata:
========================
Original URL: https://olavovieira.com.br
Prompt: Write Python code to generate a Parecer Técnico de Avaliação Mercadológica (PTAM) document for real estate valuation, ensuring compliance with ABNT NBR 14.653 and COFECI Resolution No. 1.066/07.
Generated: DETERMINISTIC_476bbc9bcafd5c86
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum

class TipoImovel(Enum):
    RESIDENCIAL = "Residencial"
    COMERCIAL = "Comercial"
    INDUSTRIAL = "Industrial"
    RURAL = "Rural"
    TERRENO = "Terreno"

@dataclass
class Endereco:
    logradouro: str
    numero: str
    complemento: Optional[str]
    bairro: str
    cidade: str
    estado: str
    cep: str

@dataclass
class CaracteristicaImovel:
    area_total: float
    area_construida: float
    quartos: int
    banheiros: int
    vagas_garagem: int
    idade: int
    conservacao: str  # Excelente, Bom, Regular, Ruim
    observacoes: Optional[str]

@dataclass
class MetodologiaAvaliacao:
    metodo: str  # Comparativo, Custo, Renda
    descricao: str
    fontes_pesquisa: List[str]
    parametros_considerados: List[str]

@dataclass
class Avaliador:
    nome: str
    creci: str
    documento: str
    telefone: str
    email: str

@dataclass
class Proprietario:
    nome: str
    documento: str
    telefone: str
    email: Optional[str]

@dataclass
class ComparativoMercado:
    imovel_referencia: str
    endereco: Endereco
    valor: float
    diferencas: List[str]
    similaridade: float  # 0-100%

class PTAMGenerator:
    def __init__(self):
        self.template = """
        PARECER TÉCNICO DE AVALIAÇÃO MERCADOLÓGICA (PTAM)
        (Conforme ABNT NBR 14.653 e Resolução COFECI 1.066/07)

        1. IDENTIFICAÇÃO DO IMÓVEL
        Tipo: {tipo_imovel}
        Endereço: {endereco_completo}
        Matrícula/Registro: {matricula}
        Proprietário: {proprietario_nome} (CPF/CNPJ: {proprietario_documento})

        2. CARACTERÍSTICAS DO IMÓVEL
        Área Total: {area_total} m²
        Área Construída: {area_construida} m²
        Quartos: {quartos}
        Banheiros: {banheiros}
        Vagas de Garagem: {vagas_garagem}
        Idade: {idade} anos
        Estado de Conservação: {conservacao}
        Observações: {observacoes_imovel}

        3. METODOLOGIA DE AVALIAÇÃO
        Método Utilizado: {metodo_avaliacao}
        Descrição: {descricao_metodo}
        Fontes de Pesquisa: {fontes_pesquisa}
        Parâmetros Considerados: {parametros_considerados}

        4. ANÁLISE COMPARATIVA DE MERCADO
        {tabela_comparativa}

        5. CONCLUSÃO
        Valor de Mercado Estimado: R$ {valor_estimado}
        Limitações e Condicionantes: {limitacoes}
        Data da Avaliação: {data_avaliacao}
        Validade: {validade}

        6. IDENTIFICAÇÃO DO AVALIADOR
        Nome: {avaliador_nome}
        CRECI: {avaliador_creci}
        Documento: {avaliador_documento}
        Contato: {avaliador_telefone} | {avaliador_email}

        Observações Finais: {observacoes_finais}
        """

    def _format_endereco(self, endereco: Endereco) -> str:
        complemento = f", {endereco.complemento}" if endereco.complemento else ""
        return f"{endereco.logradouro}, {endereco.numero}{complemento}, {endereco.bairro}, {endereco.cidade}/{endereco.estado}, CEP: {endereco.cep}"

    def _generate_comparative_table(self, comparativos: List[ComparativoMercado]) -> str:
        table = ["| Imóvel Referência | Endereço | Valor | Similaridade | Diferenças |",
                "|------------------|----------|-------|--------------|------------|"]
        
        for comp in comparativos:
            diffs = "; ".join(comp.diferencas)
            table.append(f"| {comp.imovel_referencia} | {self._format_endereco(comp.endereco)} | R$ {comp.valor:,.2f} | {comp.similaridade}% | {diffs} |")
        
        return "\n".join(table)

    def generate(
        self,
        tipo_imovel: TipoImovel,
        endereco: Endereco,
        matricula: str,
        proprietario: Proprietario,
        caracteristicas: CaracteristicaImovel,
        metodologia: MetodologiaAvaliacao,
        comparativos: List[ComparativoMercado],
        valor_estimado: float,
        limitacoes: str,
        avaliador: Avaliador,
        observacoes_finais: str = "Nenhuma observação adicional."
    ) -> str:
        data_avaliacao = datetime.date.today().strftime("%d/%m/%Y")
        validade = (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y")
        
        return self.template.format(
            tipo_imovel=tipo_imovel.value,
            endereco_completo=self._format_endereco(endereco),
            matricula=matricula,
            proprietario_nome=proprietario.nome,
            proprietario_documento=proprietario.documento,
            area_total=caracteristicas.area_total,
            area_construida=caracteristicas.area_construida,
            quartos=caracteristicas.quartos,
            banheiros=caracteristicas.banheiros,
            vagas_garagem=caracteristicas.vagas_garagem,
            idade=caracteristicas.idade,
            conservacao=caracteristicas.conservacao,
            observacoes_imovel=caracteristicas.observacoes or "Nenhuma",
            metodo_avaliacao=metodologia.metodo,
            descricao_metodo=metodologia.descricao,
            fontes_pesquisa=", ".join(metodologia.fontes_pesquisa),
            parametros_considerados=", ".join(metodologia.parametros_considerados),
            tabela_comparativa=self._generate_comparative_table(comparativos),
            valor_estimado=f"{valor_estimado:,.2f}",
            limitacoes=limitacoes,
            data_avaliacao=data_avaliacao,
            validade=validade,
            avaliador_nome=avaliador.nome,
            avaliador_creci=avaliador.creci,
            avaliador_documento=avaliador.documento,
            avaliador_telefone=avaliador.telefone,
            avaliador_email=avaliador.email,
            observacoes_finais=observacoes_finais
        )

    def save_to_file(self, content: str, filename: str) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except IOError as e:
            raise Exception(f"Erro ao salvar arquivo: {str(e)}")

# Example usage
if __name__ == "__main__":
    endereco = Endereco(
        logradouro="Av. Paulista",
        numero="1000",
        complemento="Conj. 101",
        bairro="Bela Vista",
        cidade="São Paulo",
        estado="SP",
        cep="01310-100"
    )

    proprietario = Proprietario(
        nome="João da Silva",
        documento="123.456.789-00",
        telefone="(11) 99999-9999",
        email="joao@example.com"
    )

    caracteristicas = CaracteristicaImovel(
        area_total=120.5,
        area_construida=85.0,
        quartos=3,
        banheiros=2,
        vagas_garagem=1,
        idade=10,
        conservacao="Bom",
        observacoes="Reformado em 2020"
    )

    metodologia = MetodologiaAvaliacao(
        metodo="Comparativo
