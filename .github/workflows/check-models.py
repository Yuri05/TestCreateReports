#!/usr/bin/env python3
"""
Validation script for models.csv in OSP-PBPK-Model-Library
"""

import os
import sys
import csv
import requests
import json
import re
from typing import List, Tuple, Dict, Any
from datetime import datetime


class ModelValidator:
    def __init__(self):
        self.errors = []
        self.github_token = os.environ.get('GITHUB_TOKEN')
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        } if self.github_token else {}
        
    def add_error(self, message: str):
        """Add an error message to the collection"""
        self.errors.append(message)
        print(f"ERROR: {message}")
        
    def check_empty_lines(self, file_path: str) -> bool:
        """Check if file contains empty lines or lines with only blanks"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            for i, line in enumerate(lines, 1):
                if line.strip() == '':
                    self.add_error(f"Empty line or line with only blanks found at line {i}")
                    return False
            return True
        except Exception as e:
            self.add_error(f"Error reading file {file_path}: {str(e)}")
            return False
            
    def check_execute_column(self, rows: List[Dict[str, str]]) -> bool:
        """Check that Execute column contains only TRUE or FALSE"""
        valid = True
        for i, row in enumerate(rows, 2):  # Start from row 2 (after header)
            execute_value = row.get('Execute', '').strip()
            if execute_value not in ['TRUE', 'FALSE']:
                self.add_error(f"Invalid Execute value '{execute_value}' at row {i}. Must be TRUE or FALSE")
                valid = False
        return valid
                            
    def check_file_in_release(self, repo_name: str, version: str, file_path: str) -> bool:
        """Check if a file exists in a specific release tag or branch"""
        if re.fullmatch(r"\d+\.\d+", version):
            url = f"https://api.github.com/repos/Open-Systems-Pharmacology/{repo_name}/contents/{file_path}?ref=v{version}"
        else:
            url = f"https://api.github.com/repos/Open-Systems-Pharmacology/{repo_name}/contents/{file_path}?ref={version}"
        try:
            response = requests.get(url, headers=self.headers)
            return response.status_code == 200
        except Exception:
            return False

    def check_repository_validations(self, rows: List[Dict[str, str]]) -> bool:
        """Perform all repository-related validations"""
        valid = True
        
        for i, row in enumerate(rows, 2):
            repo_name = row.get('Repository name', '').strip()
            version = row.get('Released version', '').strip()
            snapshot_name = row.get('Snapshot name', '').strip()
            workflow_name = row.get('Workflow name', '').strip()
            
            if not repo_name or not version:
                continue
                                      
            # Check 3c: Snapshot file exists
            snapshot_file = f"{snapshot_name}.json"
            if not self.check_file_in_release(repo_name, version, snapshot_file):
                self.add_error(f"Snapshot name {snapshot_name} is invalid for {repo_name}")
                valid = False
                
            # Check 3d and 3e: Workflow file exists
            if not workflow_name:
                # Check for default workflow file
                if not self.check_file_in_release(repo_name, version, "Evaluation/workflow.R"):
                    self.add_error(f"The default workflow file Evaluation/workflow.R not found for {repo_name}")
                    valid = False
            else:
                # Check for specified workflow file
                if not self.check_file_in_release(repo_name, version, workflow_name):
                    self.add_error(f"The workflow file {workflow_name} not found for {repo_name}")
                    valid = False
                    
        return valid
                    
    def check_additional_projects(self, rows: List[Dict[str, str]]) -> bool:
        """Check additional projects URLs and versions"""
        valid = True
        
        for i, row in enumerate(rows, 2):
            additional_projects = row.get('Additional projects', '').strip()
            if not additional_projects:
                continue
                
            # Split by pipe and process each entry
            projects = [p.strip() for p in additional_projects.split('|') if p.strip()]
            
            for project in projects:
                # Check 5a: URL validity
                url = f"https://raw.githubusercontent.com/Open-Systems-Pharmacology/{project}"
                try:
                    response = requests.get(url, headers=self.headers)
                    if response.status_code != 200:
                        self.add_error(f"Invalid URL for additional project: {url}")
                        valid = False
                        continue
                except Exception:
                    self.add_error(f"Invalid URL for additional project: {url}")
                    valid = False
                    continue
                                        
        return valid
        
    def validate_models_csv(self, file_path: str = 'models.csv') -> bool:
        """Main validation function"""
        print(f"Validating {file_path}...")
        
        # Check 1: Empty lines
        self.check_empty_lines(file_path)
        
        # Read CSV file
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
        except Exception as e:
            self.add_error(f"Error reading CSV file: {str(e)}")
            return False
            
        # Check 2: Execute column values
        self.check_execute_column(rows)
        
        # Check 3: Repository validations
        self.check_repository_validations(rows)
                
        # Check 5: Additional projects
        self.check_additional_projects(rows)
        
        return len(self.errors) == 0
        
    def print_summary(self):
        """Print validation summary"""
        if self.errors:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s):")
            for i, error in enumerate(self.errors, 1):
                print(f"{i}. {error}")
        else:
            print("\n✅ All validations passed!")


def main():
    """Main function"""
    validator = ModelValidator()
    
    # Run validation
    success = validator.validate_models_csv()
    
    # Print summary
    validator.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
