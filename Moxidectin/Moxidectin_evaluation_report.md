# Building and evaluation of a PBPK model for moxidectin in healthy adults

| Version                                         | master-OSP12.1                                                   |
| ----------------------------------------------- | ------------------------------------------------------------ |
| based on *Model Snapshot* and *Evaluation Plan* | https://github.com/Open-Systems-Pharmacology/Moxidectin-Model/releases/tag/vmaster |
| OSP Version                                     | 12.1                                                          |
| Qualification Framework Version                 | 3.4                                                          |

This evaluation report and the corresponding PK-Sim project file are filed at:

https://github.com/Open-Systems-Pharmacology/OSP-PBPK-Model-Library/

# Table of Contents

 * [1 Introduction](#introduction)
 * [2 Methods](#methods)
   * [2.1 Modeling Strategy](#modeling-strategy)
   * [2.2 Data](#methods-data)
     * [2.2.1 In vitro / physico-chemical Data ](#invitro-and-physico-chemical-data)
     * [2.2.2 Clinical Data  ](#clinical-data)
       * [2.2.2.1 Model Building ](#model-building)
       * [2.2.2.2 Model Verification ](#model-verification)
   * [2.3 Model Parameters and Assumptions](#model-parameters-and-assumptions)
     * [2.3.1 Absorption ](#model-parameters-and-assumptions-absorption)
     * [2.3.2 Distribution ](#model-parameters-and-assumptions-distribution)
     * [2.3.3 Metabolism and Elimination ](#model-parameters-and-assumptions-metabolism-and-elimination)
     * [2.3.4 Automated Parameter Identification ](#model-parameters-and-assumptions-parameter-identification)
 * [3 Results and Discussion](#results-and-discussion)
   * [3.1 Final input parameters](#final-input-parameters)
   * [3.2 Diagnostics Plots](#diagnostics-plots)
   * [3.3 Concentration-Time Profiles](#ct-profiles)
 * [4 Conclusion](#conclusion)
 * [5 References](#main-references)

# 1 Introduction<a id="introduction"></a>

Moxidectin is a potent, broad-spectrum endectocide (antiparasitic active against endo- and ectoparasites) ([Cotreau 2003, Tan 2022](#main-references)). It is used to in the treatment of river blindness (onchocerciasis). It selectively binds to parasite GABA-A and glutamate-gated chloride ion channels, causing paralysis of the parasite. Moxidectin shows potential for the treatment of tuberculosis, but is currently not used in clinical practice for this indication. 

Moxidectin absorption reaches Tmax after 3-4h and shows a long half-life in humans ([Drugbank](#main-references)). Oral bioavailability is enhanced by lipids, but does not result in a clinically relevant food-drug interaction. The volume of distribution is 1.2 L/kg. Moxidectin is lipophilic and highly protein bound. Metabolism is mediated via CYP3A and CYP2B. Moxidectin is eliminated mainly in feces, with negligible renal elimination.

The herein presented model building and evaluation report evaluates the performance of the PBPK model for moxidectin in (healthy) adults. The aim of this work was to establish a model that can be used to evaluate moxidectin use in tuberculosis.

The presented moxidectin PBPK model as well as the respective evaluation plan and evaluation report are provided open-source (https://github.com/Open-Systems-Pharmacology/Moxidectin-Model).

 

# 2 Methods<a id="methods"></a>

## 2.1 Modeling Strategy<a id="modeling-strategy"></a>

The general concept of building a PBPK model has previously been described by Kuepfer et al. ([Kuepfer 2016](#main-references)). Information regarding the relevant anthropometric (height, weight) and physiological parameters (e.g. blood flows, organ volumes, binding protein concentrations, hematocrit, cardiac output) in adults was gathered from the literature and has been previously published ([PK-Sim Ontogeny Database Version 7.3](#main-references)). The information was incorporated into PK-Sim® and was used as default values for the simulations in adults.

The  applied activity and variability of plasma proteins and active processes that are integrated into PK-Sim® are described in the publicly available PK-Sim® Ontogeny Database Version 7.3 ([Schlender 2016](#main-references)) or otherwise referenced for the specific process.

First, a base mean model was built using clinical Phase I data including single dose oral administration of moxidectin solution in fasted and fed state, as well as single dose oral administration as solution or tablet was used to find an appropriate structure to describe the pharmacokinetics in plasma ([Korth-Bradley 2012b](#main-references)). The mean PBPK model was developed using individuals matching the study demographics. The relative tissue specific expressions of CYP3A4 was considered. The aim of the current work was to establish a PBPK model of moxidectin for its use in tuberculosis. Although moxidectin is not approved yet for this indication, a daily dosing regimen is generally the standard for tuberculosis. Therefore, the model development prioritized prediction of the first day(s) compared to the terminal phase. 

Unknown parameters (see below) were identified using the Parameter Identification module provided in PK-Sim®. Structural model selection was mainly guided by visual inspection of the resulting description of data and biological plausibility. 

Moxidectin is absorbed relatively quickly (Tmax after 3-4h) ([Drugbank](#main-references)). For simplicity, a dissolved formulation was applied for both solution and tablet formulations.

The model was then verified by simulating ([Cotreau 2003, Kinrade 2018](#main-references)):

- a dose range between 3 mg and 36 mg 
- fed and fasted state

Details about input data (physicochemical, *in vitro* and clinical) can be found in  [Section 2.2](#methods-data).

Details about the structural model and its parameters can be found in  [Section 2.3](#model-parameters-and-assumptions).

## 2.2 Data<a id="methods-data"></a>

### 2.2.1 In vitro / physico-chemical Data <a id="invitro-and-physico-chemical-data"></a>

A literature search was performed to collect available information on physicochemical properties of moxidectin. The obtained information from literature is summarized in the table below. 

| **Parameter**   | **Unit** | **Value** | Source                                     | **Description**                                 |
| :-------------- | -------- | --------- | ------------------------------------------ | ----------------------------------------------- |
| MW              | g/mol    | 639.83          | [Drugbank](#main-references)               | Molecular weight                                |
| pK<sub>a</sub>  | - (neutral)         |           | [Wood 2024](#main-references)         | Acid dissociation constant                      |
| Solubility (pH 7) | mg/mL         | 5.20E-3          | [Drugbank](#main-references)               | Aqueous Solubility, FaSSIF, ...                 |
| logP            |          | 6          | [Drugbank](#main-references) (experimental) | Partition coefficient between octanol and water |
| logP            |          | 5.3          | [Drugbank](#main-references) (predicted) | Partition coefficient between octanol and water |
| logP            |          | 5.67          | [Wood 2024](#main-references) (predicted) | Partition coefficient between octanol and water |
| logP            |          | 4.3          | [Pubchem](#main-references) (predicted) | Partition coefficient between octanol and water |
| fu              |         | 0.00078          | [Wood 2024](#main-references)                | Fraction unbound in plasma                      |
| CLint CYP3A4            | µL/min/mg protein         | 36          | [Wood 2024](#main-references) (predicted) | Intrinsic clearance mediated by CYP3A4 |

### 2.2.2 Clinical Data  <a id="clinical-data"></a>

A literature search was performed to collect available clinical data on moxidectin in healthy adults.

#### 2.2.2.1 Model Building <a id="model-building"></a>

The following studies were used for model building (training data):

| Publication                 | Arm / Treatment / Information used for model building |
| :-------------------------- | :---------------------------------------------------- |
| [Korth-Bradley 2012a](#main-references) | Healthy Subjects with a single oral dose of 10 mg solution in fasted or fed conditions           |
| [Korth-Bradley 2012b](#main-references) | Healthy Subjects with a single oral dose of 10 mg solution or tablet           |

Data for [Korth-Bradley 2012a](#main-references) and [Korth-Bradley 2012b](#main-references) was extracted from the study reports S101 and S1005, respectively. 

#### 2.2.2.2 Model Verification <a id="model-verification"></a>

The following studies were used for model verification:

| Publication                 | Arm / Treatment / Information used for model building |
| :-------------------------- | :---------------------------------------------------- |
| [Cotreau 2003](#main-references) | Healthy Subjects with a single oral dose of 3 mg, 9 mg, 18 mg or 36 mg in fasted or fed conditions|
| [Kinrade 2018](#main-references) | Healthy Subjects with a single oral dose of 4 mg, 8 mg, 16 mg, 24 mg, 36 mg in fasted conditions      |

Data for [Kinrade 2018](#main-references) was extracted from the study report S1008.

## 2.3 Model Parameters and Assumptions<a id="model-parameters-and-assumptions"></a>

### 2.3.1 Absorption <a id="model-parameters-and-assumptions-absorption"></a>

The model parameter `Specific intestinal permeability` was calculated by default based on the lipophilicity. Predicted aqueous solubility ([Drugbank](#main-references), see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)) was set as default solubility. For simplicity, all oral administrations were modelled as solution. Food effects were not specifically evaluated, as they did not result in clinically significant effect. Nevertheless, data for fasted and fed conditions were used to develop and verify the PBPK model. For fed conditions, a standard high-fat breakfast event was implemented according to the study information.

### 2.3.2 Distribution <a id="model-parameters-and-assumptions-distribution"></a>

Fraction unbound was reported approximately 0.00078 ([Wood 2024](#main-references), see [Section 2.2.1](#221-in-vitro-and-physicochemical-data)). `Lipophilicity` was optimized within the range of measured values (4.30-6.00) to find a best match of simulated to observed moxidectin PK profile data ([Korth-Bradley 2012a, Korth-Bradley 2012b](#main-references)). After testing the available organ-plasma partition coefficient and cell permeability calculation methods built in PK-Sim®, observed clinical data was best described by choosing the partition coefficient calculation by `PK-Sim Standard` and cellular permeability calculation by `PK-Sim Standard` for moxidectin.

### 2.3.3 Metabolism and Elimination <a id="model-parameters-and-assumptions-metabolism-and-elimination"></a>

Data regarding metabolism and elimination of moxidectin is limited. Retrograde calculation of clearance, assuming 7% of clearance is CYP3A4-mediated, resulted in an intrinsic clearance of 36 µL/min/mg protein ([Wood 2024](#main-references)). The majority of clearance (93%) was assumed to be biliary clearance. Retrograde calculation based on an apparent total clearance of 2760-3506 mL/h for healthy volunteers results in an estimated biliary clearance of 40 mL/h/kg ([FDA 2018](#main-reference)). 

### 2.3.4 Automated Parameter Identification <a id="model-parameters-and-assumptions-parameter-identification"></a>

This is the result of the final parameter identification.

| Model Parameter      | Optimized Value | Unit |
| -------------------- | --------------- | ---- |
| `Lipophilicity` | 4.60                | Log units     |

# 3 Results and Discussion<a id="results-and-discussion"></a>

The PBPK model for moxidectin was developed and verified with clinical pharmacokinetic data.

The model was evaluated covering data from studies including in particular ([Korth-Bradley 2012a, Korth-Bradley 2012b, Cotreau 2003, Kinrade 2018](#main-references))

* oral administration (solution or tablet)
* a dose range between 3 mg and 36 mg 
* fed and fasted state

The model quantifies metabolism via biliary clearance and CYP3A4. 

The PBPK model was able to capture the PK of moxidectin over the first days, but not the late phase as indicated by the GMFE. As the standard dosing regimen for tuberculosis is once daily (i.e., based on dosing regimens of other tuberculosis medicines, since moxidectin is not approved for tuberculosis yet), the model is fit for purpose to evaluate moxidectin in treatment of tuberculosis. Nevertheless, further model refinement is required to describe the late phase.

The next sections show:

1. the final model parameters for the building blocks: [Section 3.1](#final-input-parameters).
2. the overall goodness of fit: [Section 3.2](#diagnostics-plots).
3. simulated vs. observed concentration-time profiles for the clinical studies used for model building and for model verification: [Section 3.3](#ct-profiles).

## 3.1 Final input parameters<a id="final-input-parameters"></a>

The compound parameter values of the final PBPK model are illustrated below.

### Compound: Moxidectin

#### Parameters

Name                                       | Value                  | Value Origin                                                                                                          | Alternative | Default
------------------------------------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------- | -------
Solubility at reference pH                 | 0.0052 mg/ml           | Unknown-Drugbank ALOGPS                                                                                               | Measurement | True   
Reference pH                               | 7                      | Unknown-Drugbank ALOGPS                                                                                               | Measurement | True   
Lipophilicity                              | 4.5953885122 Log Units | Parameter Identification-Parameter Identification-Value updated from 'Parameter Identification 1' on 2025-05-16 16:40 | Measurement | True   
Fraction unbound (plasma, reference value) | 0.00078                | Unknown-Woods 2024                                                                                                    | Measurement | True   
Is small molecule                          | Yes                    |                                                                                                                       |             |        
Molecular weight                           | 639.83 g/mol           |                                                                                                                       |             |        
Plasma protein binding partner             | Albumin                |                                                                                                                       |             |        

#### Calculation methods

Name                    | Value          
----------------------- | ---------------
Partition coefficients  | PK-Sim Standard
Cellular permeabilities | PK-Sim Standard

#### Processes

##### Metabolizing Enzyme: CYP3A4-Wood 2024

Molecule: CYP3A4

###### Parameters

Name                             | Value                     | Value Origin     
-------------------------------- | ------------------------- | -----------------
In vitro CL for liver microsomes | 36 µl/min/mg mic. protein | Unknown-Wood 2024

##### Systemic Process: Biliary Clearance-Assumption

Species: Human

###### Parameters

Name                          | Value       | Value Origin      
----------------------------- | ----------- | ------------------
Fraction unbound (experiment) | 0.00078     |                   
Lipophilicity (experiment)    | 6 Log Units |                   
Plasma clearance              | 40 ml/h/kg  | Unknown-Assumption

## 3.2 Diagnostics Plots<a id="diagnostics-plots"></a>

Below you find the goodness-of-fit visual diagnostic plots for the PBPK model performance of all data used presented in [Section 2.2.2](#clinical-data).

The first plot shows observed versus simulated plasma concentration, the second weighted residuals versus time. 

<a id="table-3-1"></a>

**Table 3-1: GMFE for Goodness of fit plot for concentration in plasma**

|Group                                    |GMFE |
|:----------------------------------------|:----|
|Moxidectin (model building)              |3.69 |
|Moxidectin (model building) 24h only     |1.20 |
|Moxidectin (model verification)          |2.87 |
|Moxidectin (model verification) 24h only |1.32 |
|All                                      |2.36 |

<br>
<br>

<a id="figure-3-1"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/2_gof_plot_predictedVsObserved.png)

**Figure 3-1: Goodness of fit plot for concentration in plasma**

<br>
<br>

<a id="figure-3-2"></a>

![](images/006_section_results-and-discussion/008_section_diagnostics-plots/3_gof_plot_residualsOverTime.png)

**Figure 3-2: Goodness of fit plot for concentration in plasma**

<br>
<br>

## 3.3 Concentration-Time Profiles<a id="ct-profiles"></a>

Simulated versus observed concentration-time profiles of all data listed in [Section 2.2.2](#clinical-data) are presented below.

<a id="figure-3-3"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/1_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_10mg_solution.png)

**Figure 3-3: Korth-Bradley 2012_PO_10mg_solution**

<br>
<br>

<a id="figure-3-4"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/2_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_10mg_solution.png)

**Figure 3-4: Korth-Bradley 2012_PO_10mg_solution 24h**

<br>
<br>

<a id="figure-3-5"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/3_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_10mg_tablet.png)

**Figure 3-5: Korth-Bradley 2012_PO_10mg_tablet**

<br>
<br>

<a id="figure-3-6"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/4_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_10mg_tablet.png)

**Figure 3-6: Korth-Bradley 2012_PO_10mg_tablet 24h**

<br>
<br>

<a id="figure-3-7"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/5_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_8mg_fasted.png)

**Figure 3-7: Korth-Bradley 2012_PO_8mg_fasted**

<br>
<br>

<a id="figure-3-8"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/6_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_8mg_fasted.png)

**Figure 3-8: Korth-Bradley 2012_PO_8mg_fasted 24h**

<br>
<br>

<a id="figure-3-9"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/7_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_8mg_fed.png)

**Figure 3-9: Korth-Bradley 2012_PO_8mg_fed**

<br>
<br>

<a id="figure-3-10"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/8_time_profile_plot_Moxidectin_Korth_Bradley_2012_PO_8mg_fed.png)

**Figure 3-10: Korth-Bradley 2012_PO_8mg_fed 24h**

<br>
<br>

<a id="figure-3-11"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/9_time_profile_plot_Moxidectin_Cotreau_2003_PO_18mg_solution_fasted.png)

**Figure 3-11: Cotreau 2003_PO_18mg_solution_fasted**

<br>
<br>

<a id="figure-3-12"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/10_time_profile_plot_Moxidectin_Cotreau_2003_PO_18mg_solution_fasted.png)

**Figure 3-12: Cotreau 2003_PO_18mg_solution_fasted 24h**

<br>
<br>

<a id="figure-3-13"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/11_time_profile_plot_Moxidectin_Cotreau_2003_PO_36mg_solution_fasted.png)

**Figure 3-13: Cotreau 2003_PO_36mg_solution_fasted**

<br>
<br>

<a id="figure-3-14"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/12_time_profile_plot_Moxidectin_Cotreau_2003_PO_36mg_solution_fasted.png)

**Figure 3-14: Cotreau 2003_PO_36mg_solution_fasted 24h**

<br>
<br>

<a id="figure-3-15"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/13_time_profile_plot_Moxidectin_Cotreau_2003_PO_36mg_solution_fed.png)

**Figure 3-15: Cotreau 2003_PO_36mg_solution_fed**

<br>
<br>

<a id="figure-3-16"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/14_time_profile_plot_Moxidectin_Cotreau_2003_PO_36mg_solution_fed.png)

**Figure 3-16: Cotreau 2003_PO_36mg_solution_fed 24h**

<br>
<br>

<a id="figure-3-17"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/15_time_profile_plot_Moxidectin_Cotreau_2003_PO_3mg_solution_fasted.png)

**Figure 3-17: Cotreau 2003_PO_3mg_solution_fasted**

<br>
<br>

<a id="figure-3-18"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/16_time_profile_plot_Moxidectin_Cotreau_2003_PO_3mg_solution_fasted.png)

**Figure 3-18: Cotreau 2003_PO_3mg_solution_fasted 24h**

<br>
<br>

<a id="figure-3-19"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/17_time_profile_plot_Moxidectin_Cotreau_2003_PO_9mg_solution_fasted.png)

**Figure 3-19: Cotreau 2003_PO_9mg_solution_fasted**

<br>
<br>

<a id="figure-3-20"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/18_time_profile_plot_Moxidectin_Cotreau_2003_PO_9mg_solution_fasted.png)

**Figure 3-20: Cotreau 2003_PO_9mg_solution_fasted 24h**

<br>
<br>

<a id="figure-3-21"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/19_time_profile_plot_Moxidectin_Cotreau_2003_PO_9mg_solution_fed.png)

**Figure 3-21: Cotreau 2003_PO_9mg_solution_fed**

<br>
<br>

<a id="figure-3-22"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/20_time_profile_plot_Moxidectin_Cotreau_2003_PO_9mg_solution_fed.png)

**Figure 3-22: Cotreau 2003_PO_9mg_solution_fed 24h**

<br>
<br>

<a id="figure-3-23"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/21_time_profile_plot_Moxidectin_Kinrade_2018_PO_16_mg.png)

**Figure 3-23: Kinrade 2018_PO_16 mg**

<br>
<br>

<a id="figure-3-24"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/22_time_profile_plot_Moxidectin_Kinrade_2018_PO_16_mg.png)

**Figure 3-24: Kinrade 2018_PO_16 mg 24h**

<br>
<br>

<a id="figure-3-25"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/23_time_profile_plot_Moxidectin_Kinrade_2018_PO_24_mg.png)

**Figure 3-25: Kinrade 2018_PO_24 mg**

<br>
<br>

<a id="figure-3-26"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/24_time_profile_plot_Moxidectin_Kinrade_2018_PO_24_mg.png)

**Figure 3-26: Kinrade 2018_PO_24 mg 24h**

<br>
<br>

<a id="figure-3-27"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/25_time_profile_plot_Moxidectin_Kinrade_2018_PO_36_mg.png)

**Figure 3-27: Kinrade 2018_PO_36 mg**

<br>
<br>

<a id="figure-3-28"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/26_time_profile_plot_Moxidectin_Kinrade_2018_PO_36_mg.png)

**Figure 3-28: Kinrade 2018_PO_36 mg 24h**

<br>
<br>

<a id="figure-3-29"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/27_time_profile_plot_Moxidectin_Kinrade_2018_PO_4_mg.png)

**Figure 3-29: Kinrade 2018_PO_4 mg**

<br>
<br>

<a id="figure-3-30"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/28_time_profile_plot_Moxidectin_Kinrade_2018_PO_4_mg.png)

**Figure 3-30: Kinrade 2018_PO_4 mg 24h**

<br>
<br>

<a id="figure-3-31"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/29_time_profile_plot_Moxidectin_Kinrade_2018_PO_8_mg.png)

**Figure 3-31: Kinrade 2018_PO_8 mg**

<br>
<br>

<a id="figure-3-32"></a>

![](images/006_section_results-and-discussion/009_section_ct-profiles/30_time_profile_plot_Moxidectin_Kinrade_2018_PO_8_mg.png)

**Figure 3-32: Kinrade 2018_PO_8 mg 24h**

<br>
<br>

# 4 Conclusion<a id="conclusion"></a>

The herein presented PBPK model adequately describes the pharmacokinetics of moxidectin in adults.

In particular, it applies metabolism and elimination via biliary clearance and CYP3A4-mediated metabolism. The PBPK model is verified for the first day(s) after administration. Thus, the model is fit for purpose to be applied for predictions of AUC and Cmax in the first days (e.g. in application such as tuberculosis), but further refinement is suggested for evaluation of the terminal half-life.

# 5 References<a id="main-references"></a>

**Cotreau 2003** Cotreau MM, Warren S, Ryan JL, Fleckenstein L, Vanapalli SR, Brown KR, Rock D, Chen CY, Schwertschlag US. The antiparasitic moxidectin: safety, tolerability, and pharmacokinetics in humans. J Clin Pharmacol. 2003 Oct;43(10):1108-15. doi: 10.1177/0091270003257456.

**FDA 2018** U.S. Food and Drug Administration. (2018). Clinical pharmacology and biopharmaceutics review(s): NDA 210867 ([https://www.accessdata.fda.gov/drugsatfda_docs/nda/2018/210867Orig1s000ClinPharmR.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2018/210867Orig1s000ClinPharmR.pdf))

**Drugbank** DrugBank DB11431 https://go.drugbank.com/drugs/DB11431, accessed 27-06-2025.

**Kinrade 2018** Kinrade SA, Mason JW, Sanabria CR, Rayner CR, Bullock JM, Stanworth SH, Sullivan MT. Evaluation of the Cardiac Safety of Long-Acting Endectocide Moxidectin in a Randomized Concentration-QT Study. Clin Transl Sci. 2018 Nov;11(6):582-589. doi: 10.1111/cts.12583.

**Korth-Bradley 2012a** Korth-Bradley JM, Parks V, Chalon S, Gourley I, Matschke K, Cailleux K, Fitoussi S, Fleckenstein L. The effect of a high-fat breakfast on the pharmacokinetics of moxidectin in healthy male subjects: a randomized phase I trial. Am J Trop Med Hyg. 2012 Jan;86(1):122-125. doi: 10.4269/ajtmh.2012.11-0415.

**Korth-Bradley 2012b** Korth-Bradley JM, Parks V, Patat A, Matschke K, Mayer P, Fleckenstein L. Relative Bioavailability of Liquid and Tablet Formulations of the Antiparasitic Moxidectin. Clin Pharmacol Drug Dev. 2012 Jan;1(1):32-7. doi: 10.1177/2160763X11432508. 

**Kuepfer 2016** Kuepfer L, Niederalt C, Wendl T, Schlender JF, Willmann S, Lippert J, Block M, Eissing T, Teutonico D. Applied Concepts in PBPK Modeling: How to Build a PBPK/PD Model.CPT Pharmacometrics Syst Pharmacol. 2016 Oct;5(10):516-531. doi: 10.1002/psp4.12134. Epub 2016 Oct 19. 	

**PK-Sim Ontogeny Database Version 7.3** ([https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf](https://github.com/Open-Systems-Pharmacology/OSPSuite.Documentation/blob/38cf71b384cfc25cfa0ce4d2f3addfd32757e13b/PK-Sim%20Ontogeny%20Database%20Version%207.3.pdf))	

**Pubchem** Pubchem 9832912 https://pubchem.ncbi.nlm.nih.gov/compound/Moxidectin, accessed 27-06-2025.

**Schlender 2016** Schlender JF, Meyer M, Thelen K, Krauss M, Willmann S, Eissing T, Jaehde U. Development of a Whole-Body Physiologically Based Pharmacokinetic Approach to Assess the Pharmacokinetics of Drugs in Elderly Individuals. Clin Pharmacokinet. 2016 Dec;55(12):1573-1589. 	

**Tan 2022** Tan B, Opoku N, Attah SK, Awadzi K, Kuesel AC, Lazdins-Helds J, Rayner C, Ryg-Cornejo V, Sullivan M, Fleckenstein L. Pharmacokinetics of oral moxidectin in individuals with Onchocerca volvulus infection. PLoS Negl Trop Dis. 2022 Mar 25;16(3):e0010005. doi: 10.1371/journal.pntd.0010005.

**Wood 2024** Wood ND, Smith D, Kinrade SA, Sullivan MT, Rayner CR, Wesche D, Patel K, Rowland-Yeo K. The use of quantitative clinical pharmacology approaches to support moxidectin dosing recommendations in lactation. PLoS Negl Trop Dis. 2024 Aug 5;18(8):e0012351. doi: 10.1371/journal.pntd.0012351. 

