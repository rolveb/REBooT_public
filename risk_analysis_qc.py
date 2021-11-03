#!/usr/bin/env python
"""
# Methods for performing quality control on IceRisk analyses

## IceRisk studies
For IceRisk analysis the following resources were presented by Rolv Erlend Bredesen at the Winterwind conferences 2018 and 2019. 


[Norwegian guidelines including uncertainty estimates using strenght of knowledge indices and NUSAP elements](https://windren.se/WW2018/03_2_24_Bredesen_Norwegian_guidelines_regarding_the_risk_of_icethrow_for_the_public_Pub_v2_draft.pdf)

[A Cross cross-comparison of the IceThrower database with 10 years of SCADA](https://windren.se/WW2019/05_01_Bredesen_A_cross-comparison_of_the_IceThrower_database_with_10_years_of_SCADA_and_meteorological_forecast_data_-_What_can_we_learn_pub_v2.pdf)

A Drone campaign (winter 2021) for the WEIC project suggests ice pieces within H+D (wind turbine hub height + rotor diameter)  for 4 m/s winds are sufficient. However up to 10 m/s wind speeds were observed after icing episode before drone pictures were taken.

## The Society for Risk Analyses (SRA) guidelines

On how to make judgment on the quality of a risk analysis

[SRA-Risk-Analysis-Quality-Test-R10.pdf](https://www.sra.org/resources/)

The questions from the quality test is repeated in the survey below.
"""
import streamlit as st
import functools
radio = functools.partial(st.radio, options=['yes','no','NA', 'not answered'], index=3)

_questions = {}
def callback(key):
    if not key in _questions:
        _questions[key] = st.sidebar.container()#sidebar.empty()
    st.write(f'#### {key}')
    st.write(AQT[key])
    answer = radio('', key=key+'_answer')
    if answer == 'yes':
        _questions[key].success(key)
    elif answer == 'no':
        _questions[key].error(key)
    elif answer == 'NA':
        _questions[key].warning(f'{key}: '+st.text_input('Give reason', key=key+'_description'))

sections = ['Framing the Analysis and Its Interface With Decision Making', # A
            'Capturing the Risk Generating Process (RGP)', # B
            'Risk Communication', # C
            'Stakeholder Involvement', # D
            'Assumptions and Scope Boundary Issues', # E
            'Proactive Creation of Alternative Courses of Action', # F
            'Basis of Knowledge', # G
            'Data Limitations, Availability, Collection, Management, Verification, Validation', # H
            'Analysis Limitations', # I
            'Uncertainty: Sources, Characterization, Implications for Risk Management', # J
            'Consideration of Alternative Analysis Approaches', # K
            'Robustness and Resilience of Action Strategies', # L
            'Model and Analysis Validation and Documentation', # M
            'Reporting', # N
            'Budget and Schedule Adequacy', # O
            ]

AQT = {}

# Framing the Analysis and Its Interface With Decision Making
AQT.update({'A1': """Clarity of the goal of the analysis.
1. Is the goal of the analysis clear and clearly announced? So that all parties can work toward that same goal without special communication.
2. Is the risk/cost of falling short of that goal described? So that all parties are appropriately motivated to achieve that goal. Example goals: to assure a safe design, to develop a safe design, to select the best design, to demostrate the level of safety to others, to defend a proposed action, to evaluate insurance or risk management policies.""",
            'A2': 'Are the decisions to be supported by this risk anaysis clearly identified, including clear descriptions of the decision alternatives? Example decisions: go/no-go on a project or action, or decide among actions, strategies or policies. In some cases the goal (A1) is to defend a proposed action. In those cases the decision can be framed as between the proposed action and whatever would happen if the proposed action is not taken.',
            'A3': 'Is the risk analysis “decision focused”? That is, is the analysis specifically focused on supporting the decision makers in deciding among those decision alternatives?',
            'A4': 'Are an adequately diverse set of perspectives (i.e., different risk management and stakeholder parties) effectively consulted in the naming and framing of the risk management problem, including scoping?',
            'A5': 'Is the risk analysis positioned appropriately in the organization chart of the client? Points in the orgnization chart may range from tactical to strategic, from risk management to management to enterprise management, etc. For example, does the risk anaysis deliver results to points in that chart (perhaps several points), such that for each point, it has the appropriate funding, timing and credibility?',

            'A6': """Embedding in the Decision Process
– A6.1 Is the risk analysis fully and effectively engaged with the risk management decision makers? That includes including the decision makers effectively and intimately in problem formulation.
– A6.2 Does the risk analysis timeline effectively support specific points in decision making?""",
    'A7': """Decision Maker Focus
– A7.1 Does the risk analysis give risk management decision makers risk information customized to their perspectives? That is, is the analysis shaped to each risk manager’s ability to address the risk, e.g., stattory authority, and to his or her legal requirements?
– A7.2 Does the risk analysis support risk managment decision makers to:
» Understand the limitations of the analyses, and the implications of those limitations for their decisions?
» Make tradeoffs against “other decision factors”?
» Address flaws in the risk management processes?""",
            'A8': 'Are the analysis report formats – numerical, grapical and text – explicitly and deliberately designed to be as helpful as possible to risk management decsion makers, in combining the results of the analysis with the “other decision factors” they may face in making their decisions?',
            'A9': 'Does the risk analysis have an adequate level of breadth, depth and detail to support the risk management decisions being supported?',
            'A10': """Are societal and stakeholder acceptability systematcally evaluated in: 
– A10.1 The risk management process?
– A10.2 Any associated recommended risk managment actions?""",
            })

#Capturing the Risk Generating Process (RGP)
AQT.update({'B1': """Comprehensiveness
– B.1.1 Is there a structured taxonomy of hazards/events that is evidence of comprehensiveness? Note that “events” can include opportunities, i.e., uncetain events causing benefits.
– B1.2 Is each scenario spelled out with the causes of change and types of change?
– B1.3 Are potential hazards/events/scenarios “not on the list” (surprises, unanticipated events, often referred to as Black Swans) explicitly addressed?
– B1.4 Are the implications of such hazards/events/scenarios for risk management explicitly described?""",
            'B2': """Is the basic structure of the Risk Generating Process understood and taken into account? For example:
» Is that process linear vs. chaotic vs. complex adaptive?
» Is the basic structure of the mathematics (e.g., linear, quadratic, exponential, etc.) appropriate for that basic structure of the process?""",
            'B3': 'Is the complexity of the Risk Generating Process fully understood and taken into account in the analysis methods? This can be tested by listing all the important (for the resulting risk) causal and associative links in the RGP, then demonstrating that each of those links is accounted for in the analysis. This need not be as burdensome as it may sound, if the causal and associative links are intelligently selected.',
            'B4':  'If the context calls for detecting early warnings, is there a process used for that detection? Those early warnings include of potential surprising risk aspects, more broadly than concrete events.',
            'B5':  'Is the possibility of system changes fully consiered and recognized? As part of that: are adequate mechanisms in place to detect those changes?',
            })
            

# Risk Communication
AQT.update({'C1': 'Is communication integrated into the risk analysis following established norms, e.g., using all aspects of:'\
"""» The ISO 31000 methodology: e.g., Establishing the context, Risk Assessment (Identification, Analysis, Evaluation), Risk Treatment?
» The International Risk Governance Council (IRGC) methodology: e.g., Pre-Assessment, Management, Appraisal, Characterization & Evaluation? Key: Categorizing the knowledge about the risk, and so related to Category G, Basis of Knowledge.""",
            'C2': ' Have all considerations for effective risk commnication been applied to assure adequacy of risk communication between analysts and decision makers?'\
"""» Analysts and other stakeholders?
» Decision makers and stakeholders?
In all three cases, “adequate” means both parties agree the communication is adequate.""",
            })

# Stakeholder Involvement
AQT.update({'D1': 'Are all stakeholders systematically and effectively identified, consulted and engaged, in such a way that all stakeholders would agree that they were effectively consulted and engaged?'\
            '''\nThat extends to: 
» Considering their perceptions and concerns;
» Involvement in the naming, framing, and scoping of the risk management problem;
» Involvement in the risk management decision process;
» Involvement in the risk management implementation process.
''',})


# Assumptions and Scope Boundary Issues
AQT.update({'E1': """Are all important assumptions, and the implications of each such assumption for risk management, 
listed systematically in language clear to risk management decision makers?
Example: A major model assumed that a critical resource constraint did not apply, as a way to avoid a large analysis burden. That assumption signifcantly distorted its risk ranking of alternative threats. That distortion was not made clear to decision makers.
The issue addressed in the above AQT has a risk variant. For clarity, we place that risk variant here in a separate AQT:""",
            'E2': "Each significant assumption may include a risk that that assumption deviates from the actual Risk Generating Process in such a way that the consquences and implications of that assumption are important. For each significant assumption, has that risk been evaluated and has that risk and its possible consequences and implications been made clear to the risk management decision makers?",
            'E3': """Are all important scope boundary issues, and the implications of each scope boundary issue for risk management, been listed systematically in language clear to risk management decision makers? Some scope boundary issues may be best addressed in terms of associated assumptions. This AQT is included to highlight scope boundary issues as distinct from assumptions.
Example: A major model limited the scope of consequences considered, as a way to avoid a large analysis burden. That scope decision significantly distorted its risk ranking of alternative threats. That distortion was not made clear to decision makers.""",
            })

# Proactive Creation of Alternative Courses of Action
AQT.update({'F1': 'Are alternative courses of action systematically generated through a process of proactive, goafocused creation? In some cases, an analysis to evaluate a course of action to address a situation focuses on only one “alternative” course of action, or a small set of alternatives that has been defined by some unexamined process or a process external to the analysis. A common wisdom in decision analysis is that often the best way to address a situation is to focus on creating alternatives other than the one or few considered. This AQT is designed to promote a process of examining the  set of alternatives considered to see if one or more  better alternatives can be developed. Of particular concern: Cases where the uncertainty is such that more robust and/or resilient alternatives should be developed, and cases where action-reaction spirals among different parties may lead to unintended consequences.',
            })
           

# Basis of Knowledge
AQT.update({'G1': 'Is the basis of knowledge characterized? For example: Which inputs are empirically “objective,” which inputs are Subject Matter Expert (SME) elicitation, which inputs are based on testing, which inputs are based on modeling, which knowledge is based on argumentation and reasoning, which aspects are treated with assumptions, which analyses are broadly accepted, which analyses are one of two or more analyses that are consiered acceptable, which analyses are novel and not widely accepted? This characterization of the basis of knowledge may seem impossibly involved in the general case, but for any particular analysis it is quite feasible and of course should be spelled out.',
            'G2': 'Is the strength of knowledge characterized in terms of its adequacy to support the risk management decisions to be supported? This AQT addresses the issue: Contexts with limited factual knowledge call for risk management recommendations that take those limitations into account.',
            'G3': 'In cases where limitations of knowledge call for risk management strategies that take those limitations into account, has that been communicated to risk management decision makers in language they can understand and apply?',
            'G4': """Is the role and importance of potential surprises and unforeseen events (often referred to as Black Swans) considered? Another description of those: Events and scenarios “not on your list.” Some risk management contexts have inconsequetial or extremely improbable Black Swans as the phenomena are well understood and the uncetainties are small. In other contexts, e.g., terrorism, Black Swans can be a driving consideration, since terrorists may deliberately design attacks that are “not on the defender’s list,” Black Swans to the defender. This is a central concern and as such is also touched on in two other categories of this battery:
- Category B: Comprehensiveness of the list of hazards/events; 
– Category L: Robustness and Resilience of Action Strategies.""",
            'G5': 'Are conflicting opinions between experts consiered as a source of uncertainty and reported to decision makers? This is re-visited in Category J on uncertainty.',
            'G6': 'Has there been explicit consideration of the possbility of unconsidered knowledge (i.e., knowledge that others have, outside of the analysis group)? That is, have special measures been implemented to check for this type of knowledge (for example, the use of an independent review of the analysis)?',
            'G7': 'Has there been explicit consideration of the possbility that some events have been disregarded because of very low probabilities, although those probabilities are based on critical assumptions? That is, have special measures been implemented to check for this type of event (for example, signals and warnings concerning the existing knowledge basis)?',
            })
      
# Data limitations
AQT.update({'H1': 'Are data limitations systematically analyzed, in particular the implications of those limitations for risk management, then any implications reported to risk managers in language they can understand and apply? Examples of those limitations: Availability and       aspects of data collection.',
            'H2': 'Are the data managed with an adequate data management system that assures each piece of data is accurately logged, and that appropriate levels of QA/QC are maintained, including the ability to demostrate that adequate level of QA/QC to a third party?',
            'H3': 'Are the data tested for reproducibility?',
            'H4': 'Are the data verified for internal consistency?',
            'H5': 'Where possible, are the data validated against external points of reference? That is, are external points of reference sought, then are the data checked for consistency with those external points?',
})

# Analysis limitations
AQT.update({'I1': 'Are all analysis limitations, as they apply to the risk management problem, clearly described? That is, are the limitations of the set of calculations of the analysis, including modeling, explicitly examined, in particular as they apply to the overall risk management sitution at hand? This is as opposed to other limitations covered in two other categories of this battery: » Category G: Basis of Knowledge » Category H: Data Limitations  Notice the overall theme spanning Categories G, H and I: Any risk analysis is subject to limitations in knowledge, data and analyses. Even in the best of cases, those limitations are typically unavoidable. What is important here is that those limitations, and the implications of those limitations, be examined and clearly explained to the risk management decsion makers.',
            'I2': 'Have all calculations in the analysis been verified? That may include extensive sensitivity analyses.',
            'I3': 'Are all metric levels in results (i.e., nominal, ordinal, interval, ratio) supported by metrically valid operations beginning with the data? For example, if the results include bar charts or other formats that present ratiscale data (whether or not the analysts intended  ratio-scale presentation), are those results ratio-scale invariant to metric-allowed variations of the source data? For a specific example from experience: A major model elicited ordinal judgments of probability, then multiplied pairs of those judgments and summed those products into results numbers, presented in scatterplots and bar charts. An analysis with altenative transformations of the original data, shifted by transforms allowable for ordinal metrics, resulted in rank reversals in the bar charts. So in that case the results were not even valid as ordinal metrics.',
            })

# Uncertainty: Sources, Characterization, Implications for Risk Management
AQT.update({'J1': '''Are all of the significant uncertainties listed in one place, and characterized there, and their implictions for decisions described there, in terms risk management decision makers can understand? Do those characterizations provide clear answers on the following key questions: What is uncertain? Who is uncertain? What are the main sources of the uncetainties? How are the uncertainties represented or expressed?''',
            
            # 6 uncertainty sources
            
            # Uncertainty Native to Data (Variation):
            'J2': 'Is that aleatory uncertainty characterized in terms risk management decision makers can understand?',
            'J3': 'Is the propagation of that aleatory uncertainty into results uncertainty characterized in terms risk management decision makers can understand? That propagation should often be analyzed with extensive sensitivity analysis',
            
            # Uncertainty Due to Limitations of Data Collection: 
            'J4': 'Is that data-limitation uncertainty characterized in terms risk management decision makers can understand?',
            'J5': 'Is the propagation of that data-limitation uncertainty into results uncertainty characterized in terms risk management decision makers can understand? That propagation should often be analyzed with extensive sensitivity analysis.',
            
             # Uncertainty Arising From Expert Judgment:
            'J6': 'Is that expert-judgment uncertainty characterized in terms risk management decision makers can understand?',
            'J7': 'Is the propagation of that expert-judgment uncetainty into results uncertainty characterized in terms risk management decision makers can understand? That propagation should often be analyzed with extensive sensitivity analysis.',
            
             # Uncertainty Arising From Disagreement Among Experts:
            'J8': 'Is that expert-disagreement uncertainty characteized in terms risk management decision makers can understand?',
            'J9': 'Is the propagation of that expert-disagreement uncertainty into results uncertainty characterized in terms risk management decision makers can undestand? That propagation should often be analyzed with extensive sensitivity analysis.',

             # Uncertainty Captured by Scenarios:
            'J10': 'Are the scenarios generated in a process that strongly encourages “casting a wide net” to encopass as wide a range of scenarios as called for to capture the uncertainties? That includes “Red Team” processes as commonly understood.',
            'J11': 'Are the scenarios generated in a process that aggressively tests system interactions?',
            'J12': 'Is that scenario uncertainty characterized in terms risk management decision makers can understand?',
            'J13': 'Are the implications of that scenario uncertainty for risk management decisions characterized in terms risk management decision makers can understand?',
            
            # Model Uncertainty:
            'J14': 'Is that model uncertainty characterized in terms risk management decision makers can understand?',
            'J15': 'Are the implications of that model uncertainty for uncertainty in the results characterized in terms risk management decision makers can understand? Those implications should often be analyzed with extensive sensitivity analysis',
            
            # Combined effect
            'J16': 'Are the six sources of uncertainty just discussed combined into a representation of the combined uncertainty in the results, in terms understandable to risk management decision makers? That reprsentation should often be developed with extensive sensitivity analysis, in particular, sensitivity analyses designed to characterize the likelihood that recomended alternatives may turn out to perform less well than other alternatives. Of particular concern: Unsupported precision in results, and uncertainty bars lacking explanation of confidence levels.',
            'J17': ' Are the implications of that combined uncertainty for risk management decisions made clear to the risk management decision makers, in terms they can understand and apply in their decisions? Of particular concern: Cases where uncertainty is such that analysis should support decision makers in comparing more robust and/or resilient alternatives against alternatives that depend on particular resoltions of uncertainty to perform relatively well',
})

# Consideration of Alternative Analysis Approaches
AQT.update({'K1': 'In some cases more than one analysis approach could be applied. Are all plausible alternative anaysis approaches considered? Then was the adopted analysis approach selected in a logical process?',
})

            
# Robustness and Resilience of Action Strategies
AQT.update({'L1': 'Is the need for robustness and resilience of action strategies explicitly examined? In this context by robustness we mean the ability of a system to perform well, without adaptation, when impacted by an attack, accident, or other event. By resilience we mean the ability of a system to respond well or adapt well to an attack, accident, or other event. In both cases, “event” includes any change, disturbance, stressor, etc., both anticipated and unanticipated events. This AQT is crucial, and directly relates to Categories B (Scenarios Not On the List, central reasons for robustness and resilience), F (Proactive Creation of Alternative Courses of Action), and I (Analysis Limitations). At base, here, is the recognition that in many areas, a risk analysis cannot confidently take into consideration all scenarios that could happen. From that it follows that, unless the need for robusness and resilience is explicitly examined, the results of the analysis can fall importantly short of adequately supporting risk management decisions.',
           'L2': 'Do the recommended risk management strategies that follow from the risk analysis include the robusness and resilience called for by the situation? This AQT follows naturally from the one before, and is based on the analysis-limitation logic presented there.',
           })

# Model and Analysis Validation and Documentation            
AQT.update({'M1': 'Is the model and analysis fully validated, by normal standards of validation in the area of practice that applies?',
            'M2': 'Is the model, analysis, and validation fully docmented, so that a third party review can determine the validity of the model?'
            })

# Reporting
AQT.update({'N1': 'Are key terms defined?',
            'N2': 'Are the results explained and motivated without using abstract terms?',
            'N3': 'Are the results as expected? If not, is it explained why?',
            'N4': 'Are all possible conflicts of interest fully disclosed?',
            'N5': 'Are all funding sources and amounts fully disclosed?'})

# Budget and Schedule Adequacy
AQT['O1'] = 'Is the budget and schedule adequate to support the risk analysis at an appropriate level of quality and defensibility? Typically a case can be made for an improved analysis with a larger budget and longer schedule. In the real world there is always a trade-off between analysis quality (as defined by these AQTs), budget and schedule. But this AQT is targeted to sitations where a convincing case can be made that the analysis is too restricted by budget and/or schedule to do an adequate job of supporting the risk managment decisions at hand.'

_answers = {}
def main():
    with st.expander('Overview'):
        st.write(__doc__)
        st.write('Risk explained by the experts:')
        st.video('https://youtu.be/CbnIlLXeHw0')


    with st.expander('Risk Analysis Quality Test (RAQT)'):
        st.write('## Goals of RAQT battery')
        st.checkbox('Define and measure the quality of risk analyses supporting risk management decisons.', True)
        st.checkbox('Full disclosure of budgets, schedules, competing interests, and other decision factors', True) 
        st.checkbox('Consider every discovered shortfall as an "Opportunity To Improve"')
        st.checkbox('Awareness on shortfalls, and the implications of those shortfalls for the decision making')

        def ask_questions(group):
            _answers[group] = {key: callback(key) for key in AQT.keys() if key.startswith(group)}

    with st.expander('Take the survey'):
        st.write('Select which groups to answer in the sidebar.')
        st.write('Hit submit button after completing a group of questions to update the state. The submitted state of each answered question is shown in sidebar.')
        st.write('NA means not applicable, that means it should be accomanied by an justification if not obvious.')
        st.write("Note that for the NA choice a text widgets to elaborate will show after the submit button has been pressed")
        st.write()
        
        st.write('Hit the download checkbox at the bottom to extract your choices.')
        st.write('\n')
        
        for i,(key,value) in enumerate(zip(list('ABCDEFGHIJKLMNO'), sections)):
            if st.sidebar.checkbox(f'{key} {sections[i]}', True):
                with st.form(key):
                    st.write(f"### Category {key} \n{value}\n")
                    ask_questions(key)
                    st.form_submit_button()
            st.write('\n')
    #with st.expander('The battery of questions'):
    #    st.write(AQT)

    if st.checkbox('Download survey'):
        survey = {key:value for key,value in st.session_state.items() if not 'FormSubmitter' in key}
        if st.checkbox('Include questions'):
            survey.update(AQT)
            survey.update(dict(zip(list('ABCDEFGHIJKLMNOP'), sections)))
        st.write(repr(survey))
        
        
if __name__ == '__main__':
    main()
