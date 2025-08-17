#!/usr/bin/env python3
"""
Generate a social media preview image for Trade Guild Consulting
Features: Logo, company name, tagline, dark background with dot pattern
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

def create_gradient_background(width, height, start_color, end_color):
    """Create a gradient background from start_color to end_color"""
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    
    # Create gradient mask
    mask = Image.new('L', (width, height))
    mask_draw = ImageDraw.Draw(mask)
    
    for y in range(height):
        alpha = int(255 * (y / height))
        mask_draw.rectangle([0, y, width, y+1], fill=alpha)
    
    # Apply gradient
    base.paste(top, (0, 0), mask)
    return base

def add_dot_pattern(image, dot_color, opacity=20):
    """Add subtle dot pattern overlay similar to services page"""
    width, height = image.size
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Create dot pattern
    dot_spacing = 40
    dot_sizes = [3, 2, 2]  # Different dot sizes for variety
    
    for y in range(0, height + dot_spacing, dot_spacing):
        for x in range(0, width + dot_spacing, dot_spacing):
            # Main dots
            if (x // dot_spacing + y // dot_spacing) % 2 == 0:
                draw.ellipse([x-dot_sizes[0], y-dot_sizes[0], x+dot_sizes[0], y+dot_sizes[0]], 
                           fill=(*dot_color, opacity))
            
            # Smaller offset dots
            offset_x, offset_y = x + dot_spacing//2, y + dot_spacing//2
            if offset_x < width and offset_y < height:
                draw.ellipse([offset_x-dot_sizes[1], offset_y-dot_sizes[1], 
                            offset_x+dot_sizes[1], offset_y+dot_sizes[1]], 
                           fill=(*dot_color, opacity//2))
    
    # Blend with original image
    return Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

def add_floating_elements(image, accent_color):
    """Add floating geometric elements like on services page"""
    width, height = image.size
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Floating circles with gradient effect
    elements = [
        (100, 150, 40, 15),  # x, y, radius, opacity
        (width-120, height-180, 60, 10),
        (width//4, height//2, 30, 8),
    ]
    
    for x, y, radius, opacity in elements:
        # Create gradient circle
        for i in range(radius, 0, -2):
            alpha = int(opacity * (i / radius))
            draw.ellipse([x-i, y-i, x+i, y+i], 
                        fill=(*accent_color, alpha))
    
    return Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

def get_font(size, bold=False):
    """Get font with fallbacks"""
    font_paths = [
        # Try system fonts
        "/System/Library/Fonts/Helvetica.ttc",  # macOS
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
        "C:\\Windows\\Fonts\\arial.ttf",  # Windows
    ]
    
    for font_path in font_paths:
        try:
            if os.path.exists(font_path):
                return ImageFont.truetype(font_path, size)
        except:
            continue
    
    # Fallback to default font
    return ImageFont.load_default()

def create_social_image():
    """Create the main social media preview image"""
    # Image dimensions for social media (1200x600 is optimal for most platforms)
    width, height = 1200, 600
    
    # Color scheme
    dark_bg = (26, 26, 26)  # Dark background similar to services page
    darker_bg = (15, 15, 15)  # Even darker for gradient
    orange_primary = (254, 144, 2)  # #FE9002
    orange_secondary = (216, 157, 64)  # #D89D40
    white = (255, 255, 255)
    light_gray = (200, 200, 200)
    
    # Create gradient background
    image = create_gradient_background(width, height, darker_bg, dark_bg)
    
    # Add dot pattern overlay
    image = add_dot_pattern(image, orange_primary, opacity=8)
    
    # Skip floating elements to remove glare effect
    # image = add_floating_elements(image, orange_primary)
    
    # Load and resize logo
    try:
        logo = Image.open('src/images/logo.png')
        # Resize logo to be even larger and more prominent
        logo_size = 280
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Position logo on the left side
        logo_x = 60
        logo_y = (height - logo_size) // 2
        
        # Paste logo directly without glow effect
        image.paste(logo, (logo_x, logo_y), logo)
        
    except Exception as e:
        print(f"Could not load logo: {e}")
        # Create a placeholder circle if logo fails to load
        draw = ImageDraw.Draw(image)
        draw.ellipse([logo_x, logo_y, logo_x + 180, logo_y + 180], 
                    fill=orange_primary, outline=white, width=3)
    
    # Add text content
    draw = ImageDraw.Draw(image)
    
    # Company name (smaller font)
    company_font = get_font(48, bold=True)
    company_text = "Trade Guild Consulting"
    
    # Position text to the right of logo, aligned with logo center
    text_x = logo_x + logo_size + 40
    text_y_start = logo_y + (logo_size // 2) - 40  # Center text vertically with logo
    
    # Add subtle shadow to text
    shadow_offset = 2
    draw.text((text_x + shadow_offset, text_y_start + shadow_offset), 
              company_text, fill=(0, 0, 0, 100), font=company_font)
    
    # Main company name
    draw.text((text_x, text_y_start), company_text, fill=white, font=company_font)
    
    # Tagline (smaller font) - now in orange
    tagline_font = get_font(28)
    tagline_text = "Business Challenges? We've Got You Covered."
    tagline_y = text_y_start + 70
    
    # Add shadow to tagline
    draw.text((text_x + shadow_offset, tagline_y + shadow_offset), 
              tagline_text, fill=(0, 0, 0, 80), font=tagline_font)
    
    # Main tagline in orange
    draw.text((text_x, tagline_y), tagline_text, fill=orange_primary, font=tagline_font)
    
    # Remove the three dots - no accent elements
    
    return image

def main():
    """Generate and save the social media image"""
    print("Generating social media preview image...")
    
    try:
        # Create the image
        social_image = create_social_image()
        
        # Save the image
        output_path = 'src/images/social-new.png'
        social_image.save(output_path, 'PNG', quality=95, optimize=True)
        
        print(f"✅ Social media image generated successfully!")
        print(f"📁 Saved to: {output_path}")
        print(f"📐 Dimensions: {social_image.size[0]}x{social_image.size[1]}px")
        
        # Also create a backup of the old image
        try:
            old_image = Image.open('src/images/social.png')
            old_image.save('src/images/social-backup.png')
            print("📋 Backup of original image created: src/images/social-backup.png")
        except:
            print("ℹ️  No existing social.png found to backup")
            
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
