# Text Summarization Project

A deep learning project that performs text summarization using the PEGASUS model. The project includes data pipeline stages from ingestion to model evaluation, with a FastAPI web interface.

## Project Structure

```
├── .github/workflows/      # CI/CD workflows
├── artifacts/             # Generated artifacts
├── config/               # Configuration files
├── logs/                 # Application logs
├── research/             # Research notebooks
├── src/                  # Source code
│   └── text_summerization/
│       ├── components/   # Core components
│       ├── config/       # Config utilities
│       ├── constants/    # Constants
│       ├── entity/       # Data classes
│       ├── pipeline/     # Training pipelines
│       └── utils/        # Utility functions
├── template.py          # Project template generator
├── app.py              # FastAPI application
├── main.py             # Training pipeline executor
├── params.yaml         # Model parameters
└── config.yaml         # Project configuration
```

## Features

- End-to-end text summarization pipeline
- Uses PEGASUS pre-trained model
- Data validation and transformation
- Model training and evaluation
- FastAPI web interface
- Containerized deployment support

## Getting Started

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Training

To run the complete training pipeline:

```bash
python main.py
```

The pipeline includes:
1. Data Ingestion
2. Data Validation  
3. Data Transformation
4. Model Training
5. Model Evaluation

### API Usage

Start the FastAPI server:

```bash
python app.py
```

The API will be available at `http://localhost:8080` with these endpoints:

- `/`: API documentation (Swagger UI)
- `/train`: Trigger training pipeline
- `/predict`: Get text summary

## Configuration

- Model parameters in `params.yaml`
- Project configuration in `config/config.yaml`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.