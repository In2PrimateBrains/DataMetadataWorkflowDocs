# Data and Metadata Management Workflow for In2PB

## Tools and services

The tools employed in and interoperable with the workflow are listed as:

### Metadata management and standardization

* odML (https://g-node.org/odml)  is an open, lightweight and flexible format that provides a common schema (with implementations in XML, JSON, YAML) to collect, organize and share metadata in a human- and machine-readable way.
* BIDS BEP032 (https://bids.neuroimaging.io/bep032) is a part of the Brain Imaging Data Structure (BIDS) extensions and is under active development. It is specifically designed for organizing, naming, and describing electrophysiological animal data. 
* BIDS BEP020 (https://bids.neuroimaging.io/bep020) is another active extension of the Brain Imaging Data Structure (BIDS). It specifies a standard for documenting eye tracking data.
* CEDAR Workbench (https://metadatacenter.org) is a web-based platform for creating, sharing, and managing metadata templates. It supports the FAIR principles and provides a user-friendly interface for metadata creation and management.
* openMINDS (https://openminds-documentation.readthedocs.io/en/latest/) is a metadata framework for linked data in neuroscience.
* LinkML (https://linkml.io/) is a general purpose modeling language that can be used with linked data, JSON, and other formalisms.

### Data representation and storage

* NIX (https://g-node.org/nix) is a lean data model and file format for storing fully annotated scientific datasets, i.e. the data together with rich metadata (odML) and their relations in a consistent, comprehensive format.
* Neo (http://neuralensemble.org/neo), provides programmatic data objects for working with and representing electrophysiological data, and can read data from many proprietary formats. In combination with NIX, Neo makes electrophysiological data interoperable with generic analysis scripts, tools and services.

### Data pre-processing and analysis

* SpikeInterface (https://spikeinterface.readthedocs.io/en/latest/) is a Python module to analyze extracellular electrophysiology data.
* Elephant (https://python-elephant.org) provides a large portfolio of standard and advanced methods for analyzing data from neuronal spike trains or time series data, such as LFPs. The Neo data model makes them easily accessible to scientists and applications.

### Data sharing and handling

* GIN (https://gin.g-node.org) is a platform for version-controlled (git and git-annex) data management and collaboration. It supports any file type and folder structure, provides both web and command-line access, option for local installation, and services including format validation and data publication (DOI).
* DataLad (https://www.datalad.org/) is a free and open source distributed data management system that keeps track of your data, creates structure, ensures reproducibility, supports collaboration, and integrates with widely used data infrastructures such as GIN.
* Snakemake (https://snakemake.github.io/) is a workflow management system that automates the execution of data pipelines. It uses a Python-based language to define rules, which specify how to create output files from input files. Snakemake determines dependencies between rules, efficiently managing workflow execution and supporting reproducibility and scalability.

## Background reading

* Grewe, J., Wachtler, T., Benda, J., 2011. A Bottom-up Approach to Data Annotation in Neurophysiology. Frontiers in Neuroinformatics 5, 16. https://doi.org/10.3389/fninf.2011.00016
* Zehl, L., Jaillet, F., Stoewer, A., Grewe, J., Sobolev, A., Wachtler, T., Brochier, T.G., Riehle, A., Denker, M., Grün, S., 2016. Handling Metadata in a Neurophysiology Laboratory. Frontiers in Neuroinformatics 10, 26. https://doi.org/10.3389/fninf.2016.00026
* Sprenger, J., Zehl, L., Pick, J., Sonntag, M., Grewe, J., Wachtler, T., Grün, S., Denker, M., 2019. odMLtables: A User-Friendly Approach for Managing Metadata of Neurophysiological Experiments. Front. Neuroinform. 13, 62. https://doi.org/10.3389/fninf.2019.00062
* Brochier, T., Zehl, L., Hao, Y., Duret, M., Sprenger, J., Denker, M., Grün, S., Riehle, A., 2018. Massively parallel recordings in macaque motor cortex during an instructed delayed reach-to-grasp task. Scientific Data 5, 180055. https://doi.org/10.1038/sdata.2018.55
* Denker, M., Grün, S., Wachtler, T., Scherberger, H., 2021. Reproducibility and efficiency in handling complex neurophysiological data. Neuroforum 27, 27–34. https://doi.org/10.1515/nf-2020-0041
