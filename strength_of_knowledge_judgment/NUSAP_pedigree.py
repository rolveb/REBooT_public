"""
Strength of knowledge assessment using NUSAP elements

https://windren.se/WW2018/03_2_24_Bredesen_Norwegian_guidelines_regarding_the_risk_of_icethrow_for_the_public_Pub_v2_draft.pdf

IceRisk 1.0 example:

With NUSAP we are able to provide numerical
statements with considerable nuance of expression.
-  Numerical, Unit, Spread, Assessment, Pedigree
-  A NUSAP element for the uncertainty on the amount of ice
debris thrown from a turbine may look like this list of values
and scores: Numeral, 8.8 tons; Unit, kg/year; Spread,
[7.5tons,10 tons]; Assessment, (High > 90 %
probability/confidence); Pedigree (3,2,3,4). Here, the Pedigree
score are given according to the following table (A) indicating
that the assessment was based on a theoretical model and
calculated data, and that this use is accepted among
colleagues, and colleagues including rebels would bring
consensus regarding the use of the model and calculated data.

"""
__author__  = 'Rolv.Bredesen'

pedigree_matrix_research = { # Funtowicz and Ravetz, 1990
    'Score':[4,3,2,1,0],
    'Theoretical Structure': ['Established theroy', 'Theory-based model', 'Computational model', 'Statistical processing', 'Definitions'],
    'Data input': ['Experimental data', 'Historic /field data', 'Calculated data', 'Educated guesses', 'Uneducated guesses'],
    'Peer-acceptance': ['Total', 'High', 'Medium', 'Low', 'None'],
    'Colleague consensus': ['All but cranks', 'All but rebels', 'Competing schools', 'Embryonic Field', 'No']
}
pedigree_assumptions = { # Flage 31.05.2017 based on van der Sluijs et al., 2005a, 2005b)
    'Score': [4,3,2,1,0],
    'Influence of situational limitations time, money etc': ['No such limitations', 'Hardly influenced', 'Moderately influenced', 'Importantly influenced', 'Completely influenced'], # important
    'Plausibility': ['Very plausible', 'Plausible', 'Acceptable', 'Hardly Plausible', 'Fictive or speculative'],
    'Choice space': ['No alternatives available', 'Very limited number of alternatives', 'Small number of alternatives', 'Average number of alternatives', 'Very ample choice of alternatives',],
    'Agreement among peers': ['Complete agreement', 'High degree of agreement', 'Competing perspectives', 'Low degree of agreement', 'Controversial'],
    'Agreement among stakeholders': ['Complete agreement', 'High degree of agreement', 'Competing perspectives', 'Low degree of agreement', 'Controversial'],
    'Sensitivity to views of analyst': ['Not sensitive', 'Hardly sensitive', 'Moderately sensitive', 'Highly sensitive', 'Extremely sensitive'], # important
    'Influence on results': ['Little or no influence', 'Local impactin the calculations', 'Important impact in a major step in the calculations', 'Moderate impact on end result', 'Important impact on end result'],
    }
    
examples = dict(
    pedigree_research_lower_bound =  [3,2,1,2],
    pedigree_research_icerisk1 = [3,2,3,4],
    pedigree_assumptions_best_practice = [4,4,3,2,3,2,1],
    pedigree_assumptions_speculative = [2,0,2,1,1,1,1],
)
