#import sys
#sys.path.append("../..")

import pyiomica as pio

from pyiomica.enrichmentAnalyses import KEGGAnalysis, ExportEnrichmentReport
from pyiomica import dataStorage as ds

EnrichmentOutputDirectory = pio.os.path.join('results', 'EnrichmentOutputDirectory', '')

#Let's do a KEGG pathway analysis for a group of genes (most in the NFKB pathway), annotated with their "Gene Symbol":
keggExample1 = KEGGAnalysis(["TAB1", "TNFSF13B", "MALT1", "TIRAP", "CHUK", "TNFRSF13C", "PARP1", "CSNK2A1", "CSNK2A2", "CSNK2B", "LTBR", "LYN", "MYD88", 
                                        "GADD45B", "ATM", "NFKB1", "NFKB2", "NFKBIA", "IRAK4", "PIAS4", "PLAU", "POLR3B", "NME1", "CTPS1", "POLR3A"])

ExportEnrichmentReport(keggExample1, AppendString='keggExample1', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The information can be computed for multiple groups, if these are provided as an association:
analysisKEGGAssociation = KEGGAnalysis({"Group1": ["C6orf57", "CD46", "DHX58", "HMGB3", "MAP3K5", "NFKB2", "NOS2", "PYCARD", "PYDC1", "SSC5D"], 
                                                    "Group2": ["TAB1", "TNFSF13B", "MALT1", "TIRAP", "CHUK", "TNFRSF13C", "PARP1", "CSNK2A1", "CSNK2A2", "CSNK2B", "LTBR", 
                                                "LYN", "MYD88", "GADD45B", "ATM", "NFKB1", "NFKB2", "NFKBIA", "IRAK4", "PIAS4", "PLAU", "POLR3B", "NME1", "CTPS1", "POLR3A"]})
        
ExportEnrichmentReport(analysisKEGGAssociation, AppendString='analysisKEGGAssociation', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The data can be computed with or without a label. If labeled, the gene ID must be the first element for each ID provided. The data is in the form {ID,label}:
analysisKEGGLabel = KEGGAnalysis([["C6orf57", "Protein"], ["CD46", "Protein"], ["DHX58", "Protein"], ["HMGB3", "Protein"], ["MAP3K5", "Protein"], 
                                            ["NFKB2", "Protein"], ["NOS2", "Protein"], ["PYCARD", "Protein"], ["PYDC1","Protein"], ["SSC5D", "Protein"]])

ExportEnrichmentReport(analysisKEGGLabel, AppendString='analysisKEGGLabel', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The same result is obtained if IDs are enclosed in list brackets:
analysisKEGGNoLabel = KEGGAnalysis([["C6orf57"], ["CD46"], ["DHX58"], ["HMGB3"], ["MAP3K5"], ["NFKB2"], ["NOS2"], ["PYCARD"], ["PYDC1"], ["SSC5D"]])

ExportEnrichmentReport(analysisKEGGNoLabel, AppendString='analysisKEGGNoLabel', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The same result is obtained if IDs are input as strings:
analysisKEGGstrings = KEGGAnalysis(["C6orf57", "CD46", "DHX58", "HMGB3", "MAP3K5", "NFKB2", "NOS2", "PYCARD", "PYDC1", "SSC5D"])

ExportEnrichmentReport(analysisKEGGstrings, AppendString='analysisKEGGstrings', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The data can be mixed, e.g. proteins and RNA with different labels:
analysisKEGGMixed = KEGGAnalysis([["C6orf57", "Protein"], ["CD46", "Protein"], ["DHX58", "Protein"], ["HMGB3", "RNA"], ["HMGB3", "Protein"], ["MAP3K5", "Protein"], 
                                            ["NFKB2", "RNA"], ["NFKB2", "Protein"], ["NOS2", "RNA"], ["PYCARD", "RNA"], ["PYDC1", "Protein"], ["SSC5D", "Protein"]])

ExportEnrichmentReport(analysisKEGGMixed, AppendString='analysisKEGGMixed', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#The data in this case treated as originating from a single population. Protein and RNA labeled data for the same identifier are treated as equivalent.
#We can instead treat the data as different by setting the MultipleList and MultipleListCorrection options:
analysisKEGGMixedMulti = KEGGAnalysis([["C6orf57", "Protein"], ["CD46", "Protein"], ["DHX58", "Protein"], ["HMGB3", "RNA"], ["HMGB3", "Protein"], ["MAP3K5", "Protein"], 
                                                ["NFKB2", "RNA"], ["NFKB2", "Protein"], ["NOS2", "RNA"], ["PYCARD", "RNA"], ["PYDC1", "Protein"], ["SSC5D", "Protein"]], 
                                                MultipleList=True, MultipleListCorrection='Automatic')

ExportEnrichmentReport(analysisKEGGMixedMulti, AppendString='analysisKEGGMixedMulti', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#We can carry out a "Molecular" analysis for compound data. We consider the following metabolomics data, which has labels "Meta" 
#and additional mass and retention time information in the form {identifier,mass, retention time, label}:
compoundsExample = [["cpd:C19691", 325.2075, 10.677681, "Meta"], ["cpd:C17905", 594.2002, 8.727458, "Meta"],["cpd:C09921", 204.0784, 12.3909445, "Meta"], 
                    ["cpd:C18218", 272.2356, 13.473582, "Meta"], ["cpd:C14169", 235.1573, 12.267084, "Meta"],["cpd:C14245", 262.2296, 13.545572, "Meta"], 
                    ["cpd:C09137", 352.2615, 14.0554285, "Meta"], ["cpd:C09674", 296.1624, 12.147417, "Meta"], ["cpd:C00449", 276.1334, 11.004139, "Meta"], 
                    ["cpd:C02999", 364.1497, 12.147243, "Meta"], ["cpd:C07915", 309.194, 7.3625283, "Meta"],["cpd:C08760", 496.2309, 8.7241125, "Meta"], 
                    ["cpd:C14549", 276.0972, 11.078914, "Meta"], ["cpd:C20533", 601.3378, 12.75722, "Meta"], ["cpd:C20790", 212.1051, 7.127666, "Meta"], 
                    ["cpd:C09137", 352.2613, 12.869867, "Meta"], ["cpd:C17648", 400.2085, 10.843841, "Meta"], ["cpd:C07807", 240.1471, 0.48564285, "Meta"], 
                    ["cpd:C08564", 324.0948, 10.281, "Meta"], ["cpd:C19426", 338.2818, 13.758765, "Meta"], ["cpd:C02943", 468.3218, 14.263261, "Meta"], 
                    ["cpd:C04882", 1193.342, 14.707576, "Meta"]]

compoundsExampleKEGG = KEGGAnalysis(compoundsExample, FilterSignificant=True, AnalysisType='Molecular')

ExportEnrichmentReport(compoundsExampleKEGG, AppendString='compoundsExampleKEGG', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#We can carry out multiomics data analysis. We consider the following simple example:
multiOmicsData = [["C6orf57", "Protein"], ["CD46", "Protein"], ["DHX58", "Protein"], ["HMGB3", "RNA"], ["HMGB3", "Protein"], 
                    ["MAP3K5", "Protein"], ["NFKB2", "RNA"], ["NFKB2", "Protein"], ["NOS2", "RNA"], ["PYCARD", "RNA"], ["PYDC1", "Protein"], 
                    ["SSC5D", "Protein"], ["cpd:C19691", 325.2075, 10.677681, "Meta"], ["cpd:C17905", 594.2002, 8.727458, "Meta"], 
                    ["cpd:C09921", 204.0784, 12.3909445, "Meta"], ["cpd:C18218", 272.2356, 13.473582, "Meta"], 
                    ["cpd:C14169", 235.1573, 12.267084, "Meta"], ["cpd:C14245", 262.2296, 13.545572, "Meta"], 
                    ["cpd:C09137", 352.2615, 14.0554285, "Meta"], ["cpd:C09674", 296.1624, 12.147417, "Meta"],
                    ["cpd:C00449", 276.1334, 11.004139, "Meta"],["cpd:C02999", 364.1497, 12.147243, "Meta"],
                    ["cpd:C07915", 309.194, 7.3625283, "Meta"],["cpd:C08760", 496.2309, 8.7241125, "Meta"],
                    ["cpd:C14549", 276.0972, 11.078914, "Meta"],["cpd:C20533", 601.3378, 12.75722, "Meta"], 
                    ["cpd:C20790", 212.1051, 7.127666, "Meta"], ["cpd:C09137", 352.2613, 12.869867, "Meta"],
                    ["cpd:C17648", 400.2085, 10.843841, "Meta"], ["cpd:C07807", 240.1471, 0.48564285, "Meta"], 
                    ["cpd:C08564", 324.0948, 10.281, "Meta"], ["cpd:C19426", 338.2818, 13.758765, "Meta"], 
                    ["cpd:C02943", 468.3218, 14.263261, "Meta"], ["cpd:C04882", 1193.342, 14.707576, "Meta"]]

#We can carry out "Genomic" and "Molecular" analysis concurrently by setting AnalysisType = "All":
multiOmicsDataKEGG = KEGGAnalysis(multiOmicsData, AnalysisType='All', MultipleList=True, MultipleListCorrection='Automatic') 

ExportEnrichmentReport(multiOmicsDataKEGG, AppendString='multiOmicsDataKEGG', OutputDirectory=EnrichmentOutputDirectory + 'KEGGAnalysis/')

#Enrichment analysis function KEGGAnalysis can be used with a clustering object.
#First run examples of use of categorization functions to generate clustering objects.
#Then run "results = KEGGAnalysis(ds.read(pathToClusteringObjectOfInterest))",
#to calculate enrichment for each group in each class, and then export enrichment results to a file if necesary.