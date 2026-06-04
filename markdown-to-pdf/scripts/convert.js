#!/usr/bin/env node

const { execSync } = require('child_process');
const glob = require('glob');
const path = require('path');

// Get arguments from command line
const args = process.argv.slice(2);
const pattern = args[0] || '*.md';

// Find all matching markdown files
const files = glob.sync(pattern, { nodir: true });

if (files.length === 0) {
  console.error(`No files found matching pattern: ${pattern}`);
  process.exit(1);
}

console.log(`Found ${files.length} file(s) to convert:`);
files.forEach(file => console.log(`  - ${file}`));

// Convert each file
files.forEach(inputFile => {
  const outputFile = inputFile.replace(/\.md$/, '.pdf');

  try {
    console.log(`Converting ${inputFile} -> ${outputFile}...`);
    execSync(`npx markdown-pdf "${inputFile}" -o "${outputFile}"`, { stdio: 'inherit' });
    console.log(`✓ Successfully converted to ${outputFile}`);
  } catch (error) {
    console.error(`✗ Failed to convert ${inputFile}:`, error.message);
    process.exit(1);
  }
});

console.log(`\\nAll ${files.length} file(s) converted successfully!`);