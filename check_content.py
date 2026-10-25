"""Exit nonzero until the activity's personal content is present."""
from portfolio import content_gaps, load_profile

if __name__ == "__main__":
    gaps = content_gaps(load_profile())
    if gaps:
        print("Content needed before submission:")
        for gap in gaps:
            print("-", gap)
        raise SystemExit(1)
    print("Required content fields are present. Review accuracy and authorship before publishing.")
