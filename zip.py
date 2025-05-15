import sys
import shutil
import os

def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("APP_NAME argument is required")
            
        app_name = sys.argv[1]
        output_filename = f"{app_name}.zip"
        
        print(f"Creating archive {output_filename} from current directory")
        shutil.make_archive(app_name, 'zip', '.')
        
        if not os.path.exists(output_filename):
            raise FileNotFoundError(f"Failed to create {output_filename}")
            
        print(f"Successfully created {output_filename}")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
