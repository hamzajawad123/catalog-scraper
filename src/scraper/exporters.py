import pandas as pd
import os

def export_data(data_list):
    df = pd.DataFrame(data_list)
    # Remove duplicates based on URL
    initial_count = len(df)
    df = df.drop_duplicates(subset=['product_url'])
    duplicates_removed = initial_count - len(df)
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/products.csv', index=False)
    
    # Generate Summary
    summary = df.groupby('subcategory').agg(
        total_products=('product_title', 'count'),
        avg_price=('price', 'mean'),
        min_price=('price', 'min'),
        max_price=('price', 'max'),
        missing_descriptions=('description', lambda x: x.isna().sum() or (x == "").sum())
    ).reset_index()
    
    summary['duplicates_removed'] = duplicates_removed
    summary.to_csv('data/category_summary.csv', index=False)