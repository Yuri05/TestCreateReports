## How to create evaluation reports

- Create a new branch from the `main` branch (for instance, `my-reports`)
  - Define the models by updating `models.csv` (s. the [Models](#models) section below for details)
  - [OPTIONAL] Adjust the OSP environment and tools by updating `tools.csv` (s. the [Tools](#tools) section below for details)
  - Go to the Github Action: [Create evaluation reports and projects](../../actions/workflows/create-evaluation_reports.yml)
    - Click on the button __Run workflow__ 
      - Select your branch defined in the first step (for instance, `my-reports`)
      - [OPTIONAL] Adjust the commit message which will appear later in the created pull request
        (s. [below](#next-step))
      - Click on the green button __Run workflow__
        
        <img width="800" src="https://github.com/user-attachments/assets/863a98cd-ecff-43c5-8ed9-b1458becf48c" />

## How to create qualification reports

- Create a new branch from the `main` branch (for instance, `my-reports`)
  - Define the qualifications by updating `qualifications.csv` (s. the [Qualifications](#qualifications) section below for details)
  - [OPTIONAL] Adjust the OSP environment and tools by updating `tools.csv` (s. the [Tools](#tools) section below for details)
  - Go to the Github Action: [Qualification Reports](../../actions/workflows/create-qualification_reports.yml)
    - Click on the button __Run workflow__ 
      - Select your branch defined in the first step (for instance, `my-reports`)
      - [OPTIONAL] Adjust the commit message which will appear later in the created pull request
        (s. [below](#next-step))
      - Click on the green button __Run workflow__ 

## What to do when reports are created<a id="next-step"></a>

When the qualification reports are created, pull requests are triggered (one pull request for each qualification report) toward the branch defined in the first step (for instance, `my-reports`)
The pull requests will allow users to review the updates in the reports and adopt the new version.

## Models

The `models.csv` file indicates which models should be run and qualified.
The header includes the following fields:

- __Execute__: If `TRUE` run the qualification. If `FALSE`, skip the qualification.
- __Repository name__: Name of Github OSP repository from which to get the model, e.g. `7E3-Model` for [7E3-Model](https://github.com/Open-Systems-Pharmacology/7E3-Model)
- __Released version__: Tag version of the model, e.g. `1.0`
- __Snapshot name__: Name of the snapshot (`.json`) file, e.g. `7E3` for [7E3.json](https://github.com/Open-Systems-Pharmacology/7E3-Model/7E3.json)
- __Workflow name__: Path of workflow R script that creates the function to run the qualification if not default.
> [!TIP]
> Leave blank cell if default path, `evaluation/workflow.R`, is used (this path is case insensitive). 
- __Additional projects__: Url of additional project snapshots to export as `pksim5` projects, e.g. `Propofol-Pediatrics/refs/tags/v1.0/Propofol-Pediatrics.json`
> [!TIP]
> If multiple projects are exported, they need to be separated by a pipe character: `|`, e.g. `X-Pediatrics.json|Y-Pediatrics.json`

### Qualifications

The `qualifications.csv` file indicates which qualification plans should be processed.
The header includes the following fields:

- __Execute__: If `TRUE` run the qualification. If `FALSE`, skip the qualification.
- __Repository name__: Name of GitHub OSP repository from which to get the qualification plan, e.g. `Qualification-CKD` for https://github.com/Open-Systems-Pharmacology/Qualification-CKD.
- __Released version__: Tag version of the qualificaion plan repository, e.g. `1.0`
- __Workflow name__: Path of workflow R script that creates the function to run the qualification if not default.
> [!TIP]
> Leave blank cell if default path, `Qualification/workflow.R`, is used (this path is case insensitive).
- __Folder name__: Name of exported folder within [OSP-Qualification-Reports](https://github.com/Open-Systems-Pharmacology/OSP-Qualification-Reports) repository, e.g. `Qualification-CKD` for [OSP-Qualification-Reports/Qualification-CKD](https://github.com/Open-Systems-Pharmacology/OSP-Qualification-Reports/tree/master/Qualification-CKD)
 
## Tools 

The `tools.csv` file indicates software and software versions to be installed in environment before running the qualifications of the models.
If a link is defined in the `URL` column, the installation will use the software from the link as is instead of searching from the version.
Please ensure compatibility between their versions.
The following available tools to installed are detailed below:

- [__ospsuite-R__](https://www.open-systems-pharmacology.org/OSPSuite-R/) : R package providing the functionality of loading, manipulating, and simulating the simulations created in the Open Systems Pharmacology Software tools PK-Sim and MoBi.
- [__Reporting Engine__](https://www.open-systems-pharmacology.org/OSPSuite.ReportingEngine/): R package providing a framework in R to design and create reports evaluating PBPK models developed in the Open Systems Pharmacology ecosystem.
- [__RUtils__](https://www.open-systems-pharmacology.org/OSPSuite.RUtils/): R package providing utility functions for Open Systems Pharmacology R Packages
- [__TLF__](https://www.open-systems-pharmacology.org/TLF-Library/): R package providing an object-oriented framework to create tables and figures, which are used by R packages in the Open Systems Pharmacology ecosystem
- [DEPRECATED __rClr__](https://github.com/Open-Systems-Pharmacology/rClr): R package for accessing .NET. This package has been deprecated in favor of `{rSharp}`.
- [__rSharp__](https://www.open-systems-pharmacology.org/rSharp/): R package providing access to .NET libraries from R. It allows to create .NET objects, access their fields, and call their methods
- [__Qualification Runner__](https://github.com/Open-Systems-Pharmacology/QualificationRunner): Qualification runner in charge of managing a qualification workflow
- [__Qualification Framework__](https://docs.open-systems-pharmacology.org/shared-tools-and-example-workflows/qualification): Enables an automated validation of various scenarios (use-cases) supported by the OSP platform
- [__PK-Sim__](https://github.com/Open-Systems-Pharmacology/PK-Sim): Portable version of the comprehensive software tool for whole-body physiologically based pharmacokinetic modeling
