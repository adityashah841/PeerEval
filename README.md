# PeerEval: Estimating Informativeness in Peer Review through Paper-Review Interaction

## Overview

This repository contains the dataset, code, and supplementary materials for the paper "PeerEval: Estimating Informativeness in Peer Review through Paper-Review Interaction." This research introduces a novel metric to evaluate the informativeness of peer reviews, addressing various factors such as coverage, comprehensiveness, critique strength, and clarity. The paper proposes a computational framework leveraging techniques like lexical analysis, cross-attention mechanisms, Bi-LSTM modeling, and abstractive summarization to automate this evaluation process.

## Authors

- **Prabhat Kumar Bharti** (Department of Computer Science and Engineering, IIT Patna, Bihta Kanpa Road, Patna, Bihar, India)
- **Aditya Shah** (Department of Computer Engineering, Dwarkadas J. Sanghvi College of Engineering, Mumbai, Maharashtra, India)
- **Vijay Harkare** (Department of Computer Engineering, Dwarkadas J. Sanghvi College of Engineering, Mumbai, Maharashtra, India)
- **Riya Bihani** (Department of Computer Engineering, Dwarkadas J. Sanghvi College of Engineering, Mumbai, Maharashtra, India)
- **Mayank Agarwal** (Department of Computer Science and Engineering, IIT Patna, Bihta Kanpa Road, Patna, Bihar, India)
- **Asif Ekbal** (Department of Computer Science and Engineering, IIT Patna, Bihta Kanpa Road, Patna, Bihar, India)

## Abstract

Peer review is crucial for maintaining the quality, credibility, and integrity of research. However, challenges like bias, conflicts of interest, and inconsistency compromise its reliability. This study introduces a metric to evaluate peer review informativeness based on factors such as section coverage, comprehensiveness, critique strength, and clarity. The proposed computational framework uses lexical analysis, cross-attention mechanisms, Bi-LSTM modeling, and abstractive summarization to automate the evaluation process, aiming to reduce the manual burden on editors and uphold review integrity.

## Keywords

- Peer review
- Content analysis
- Review quality
- Informativeness metric
- Computational framework

## Repository Contents

- `dataset/`: Contains the dataset used and the informativeness score generation files used in the study.
- `model/`: Contains the scripts and models used for data processing, model training, and evaluation.

## Installation

To run the code, you need to set up the environment with the required dependencies. Use the following commands to set up the environment:

```bash
# Clone the repository
git clone https://github.com/your-repo/PeerEval.git
cd PeerEval

# Create a virtual environment
python3 -m venv env
source env/bin/activate

# Install the required packages
pip install -r requirements.txt

# Download the data from the following link. Use Webscraping.py and pdf.py to create the test set

# Run the dataset and informativeness score formation files from the dataset folder
cd datasets

# Run the files in the model folder on the dataset created to obtain the results
cd ..
cd model

